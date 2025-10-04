from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config import LLM_MODEL, GROQ_API_KEY

def build_qa_chain(vectorstore):
    """Create a QA chain with Groq + Retriever + Custom Prompt"""

    retriever = vectorstore.as_retriever(
        search_type="similarity", 
        search_kwargs={"k": 5}
    )

    llm = ChatGroq(model=LLM_MODEL, api_key=GROQ_API_KEY)

    # --- Custom Prompt ---
    template = """
    You are an expert AI assistant specialized in LangChain. 
    Use ONLY the provided context to answer the question. 
    - If the context does not have the answer, say "I don’t know based on the docs."
    - When possible, give examples in Python code.
    - Be clear and concise.

    Context:
    {context}

    Question:
    {question}

    Helpful Answer:
    """
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",   # other options: "map_reduce", "refine"
        chain_type_kwargs={"prompt": prompt}
    )

    print("✅ QA Chain with custom prompt ready")
    return qa_chain
