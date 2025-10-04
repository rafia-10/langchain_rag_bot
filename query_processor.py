import re
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config import LLM_MODEL, GROQ_API_KEY

def clean_query(query: str) -> str:
    """
    Basic text normalization.
    """
    q = query.strip()
    q = re.sub(r"\s+", " ", q)          # collapse spaces
    q = re.sub(r"[^\w\s\?]", "", q)     # remove junk chars
    return q

def rephrase_query_with_llm(query: str) -> str:
    """
    Use Groq LLM to rephrase user query into a clear question.
    """
    llm = ChatGroq(model=LLM_MODEL, api_key=GROQ_API_KEY)

    template = """
    Rewrite the following user input into a clear, well-formed technical question
    suitable for searching LangChain documentation. Keep it concise.

    Input: {query}
    Rewritten:
    """
    prompt = PromptTemplate(input_variables=["query"], template=template)

    return llm.invoke(prompt.format(query=query)).content
