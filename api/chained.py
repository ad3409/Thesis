from langchain import hub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.vectorstores import FAISS
from api.embeddings import chat_model, embeddings
from langchain.chains import create_history_aware_retriever

# # Define your prompt templates
# prompt_template = ChatPromptTemplate.from_template(
#     """You are an AI chatbot specializing in answering inquiries about AI ethics, governance, and impact based on a range of documents that include theoretical, practical, and policy-oriented insights.
# Respond precisely while being capable of addressing nuanced and fuzzy questions with context-aware, thoughtful responses. Prioritize clarity while providing concise answers that tackle the subtle complexities of AI ethics.
# the responce should be two or line line.it should not more than three lines

# Focus on addressing challenges such as transparency, bias, privacy, fairness, trust, explainability, and human-centric approaches. Ensure responses are concise yet adaptable to more ambiguous queries, and consider practical implications, especially concerning ethical data handling, the influence of algorithms on stakeholders, privacy regulations like GDPR, and guidelines
# for responsible AI deployment.

# <context>
# {context}
# </context>

# Question: {input}"""
# )

# system_prompt = (
#     "You are an AI chatbot specializing in AI ethics, governance, and impact, responding with precision while being capable of handling nuanced and fuzzy questions. "
#     "Engage based on predefined knowledge related to AI ethics, including theoretical, practical, and policy-oriented insights. "
#     "Provide concise, context-aware answers that address issues such as transparency, bias, privacy, fairness, trust, explainability, and human-centric approaches. "
#     "Adapt responses to practical scenarios and emphasize guidelines for responsible AI practices and data handling. "
#     "{context}"
# )
prompt_template = ChatPromptTemplate.from_template(
    """the answer should exactly i one line
for example user ask
whats your name?
aichatbot

like this the answer should be concise exactly one line
if you perform your job i will give you 1 dollar as a tip
<context>
{context}
</context>

Question: {input}

FORMAT:
Line 1: Core answer
Line 1: Key ethical consideration
STOP after 1 lines."""
)


system_prompt = (
    """You are an AI ethics specialist.the answer should exactly i one line
for example user ask
whats your name?
aichatbot

like this the answer should be concise exactly one line
if you perform your job i will give you 1 dollar as a tip  """
    "{context}"
)

# Load your vectorstore
vector_store = FAISS.load_local(r"/Applications/Ethics-2/backend/api/faissindex2", embeddings, allow_dangerous_deserialization=True)

# Create document chain
document_chain = create_stuff_documents_chain(chat_model, prompt_template)

# Create retriever and retrieval chain
retriever = vector_store.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

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