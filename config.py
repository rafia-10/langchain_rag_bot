import os
from dotenv import load_dotenv

# URLs of LangChain docs (the knowledge base)
DOC_URLS = [
    "https://python.langchain.com/docs/introduction/",
    "https://python.langchain.com/docs/concepts/",
    "https://python.langchain.com/docs/concepts/agents/",
    "https://python.langchain.com/docs/concepts/retrievers/",
    "https://python.langchain.com/docs/concepts/tools/",
    "https://python.langchain.com/docs/tutorials/retrievers/",
    "https://python.langchain.com/docs/how_to/",
    "https://python.langchain.com/docs/how_to/installation/"
]

# ChromaDB persist directory
VECTOR_DB_PATH = "./langchain_db"

# HuggingFace Embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# GroqAI LLM
LLM_MODEL = "llama3-8b-8192"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Did you set it in .env?")
