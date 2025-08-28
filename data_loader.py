
from langchain_community.document_loaders import WebBaseLoader
from config import DOC_URLS

def load_docs():
    """Load LangChain documentation from given URLs"""
    loader = WebBaseLoader(DOC_URLS)
    docs = loader.load()
    print(f"✅ Loaded {len(docs)} docs")
    return docs
