
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_docs(docs, chunk_size=800, chunk_overlap=50):
    """Split docs into smaller chunks for embeddings"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(docs)
    print(f"✅ Created {len(chunks)} chunks")
    return chunks
