import numpy as np
from langchain import hub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.vectorstores import FAISS
from api.embeddings import chat_model, embeddings
from langchain.chains import create_history_aware_retriever

# Define the gradient descent update rule
def update_parameters(theta, y_true, y_pred, eta, lambda_reg):
    """
    Update parameters using gradient descent.
    
    Args:
        theta (numpy array): Current model parameters (embeddings).
        y_true (numpy array): True values (ground-truth).
        y_pred (numpy array): Predicted values.
        eta (float): Learning rate.
        lambda_reg (float): Regularization term.
    
    Returns:
        numpy array: Updated model parameters.
    """
    grad_loss = np.sum((y_true - y_pred)[:, None] * np.gradient(y_pred))  # Compute gradient of loss
    grad_reg = np.gradient(np.linalg.norm(theta, ord=2))  # Compute gradient of regularization
    return theta - eta * (grad_loss + lambda_reg * grad_reg)  # Update theta

# Optimize embeddings inside FAISS vector store
def optimize_embeddings(vector_store, learning_rate=0.01, lambda_reg=0.1):
    """
    Applies gradient descent updates to embeddings in FAISS.

    Args:
        vector_store (FAISS): FAISS vector store.
        learning_rate (float): Learning rate for gradient descent.
        lambda_reg (float): Regularization term.

    Returns:
        FAISS: Updated FAISS vector store.
    """
    for doc in vector_store.docstore._dict.values():
        # Retrieve stored embeddings
        y_pred = np.array(doc['embedding'])
        y_true = y_pred  # Replace with real ground-truth labels

        # Update embeddings
        doc['embedding'] = update_parameters(
            np.array(doc['embedding']), y_true, y_pred, learning_rate, lambda_reg
        )
    return vector_store

# Load FAISS vector store
vector_store = FAISS.load_local(r"/Applications/Ethics-2/backend/api/faissindex2", embeddings, allow_dangerous_deserialization=True)

# Apply optimization before retrieval
vector_store = optimize_embeddings(vector_store)

# Define Chat Prompt Templates
prompt_template = ChatPromptTemplate.from_template(
    """the answer should be exactly one line.
Example:
User: What's your name?
AI: AIBot.

The answer should be concise, exactly one line.

<context>
{context}
</context>

Question: {input}

FORMAT:
Line 1: Core answer
STOP after 1 line."""
)

system_prompt = (
    """You are an AI ethics specialist. Your answer should be exactly one line.
Example:
User: What's your name?
AI: AIBot.

Provide concise responses.
{context}"""
)

# Create document retrieval chain
document_chain = create_stuff_documents_chain(chat_model, prompt_template)

# Create retriever
retriever = vector_store.as_retriever()

# Create history-aware retriever
history_aware_retriever = create_history_aware_retriever(
    chat_model, retriever, 
    ChatPromptTemplate.from_messages(
        [
            ("system", "Given a chat history and the latest user question..."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ]
    )
)

# Create final question-answering chain
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(chat_model, qa_prompt)

# Create RAG chain
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# Example usage
def query_ai(question):
    """
    Queries the AI system and retrieves an answer.

    Args:
        question (str): The user's question.

    Returns:
        str: AI-generated response.
    """
    return rag_chain.invoke({"input": question})

# Example query
response = query_ai("What is the importance of AI ethics?")
print(response)
