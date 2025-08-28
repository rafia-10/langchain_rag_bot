
from langchain.vectorstores import Chroma
from config import VECTOR_DB_PATH

def build_vectorstore(chunks, embeddings):
    """Create & persist a Chroma vectorstore"""
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH,
        collection_metadata={"hnsw:space": "cosine"}  # 👈 cosine similarity
    )
    print(f"✅ Vectorstore created at {VECTOR_DB_PATH}")
    return vectorstore
