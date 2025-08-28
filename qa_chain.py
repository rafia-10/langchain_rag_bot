from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from config import LLM_MODEL, GROQ_API_KEY

def build_qa_chain(vectorstore):
    """Create a QA chain with Groq + Retriever"""
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    llm = ChatGroq(model=LLM_MODEL,
                   api_key=GROQ_API_KEY)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    print("✅ QA Chain ready")
    return qa_chain
