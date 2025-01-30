from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from api.config import GOOGLE_API_KEY
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
# Initialize embeddings and chat model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)

# chat_model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     google_api_key=GOOGLE_API_KEY
# )


apikey="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"
chat_model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

# Specify the repo_id for the T5 model
# repo_id = "mistralai/Mistral-7B-Instruct-v0.3"  # or "t5-small", "t5-base", etc., depending on your needs

# # Initialize the HuggingFaceHub with the T5 model
# chat_model = HuggingFaceHub(
#     huggingfacehub_api_token=apikey,
#     repo_id=repo_id,
# )
