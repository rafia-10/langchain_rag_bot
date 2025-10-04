from langchain.evaluation.qa import QAEvalChain
from langchain_groq import ChatGroq
from config import LLM_MODEL, GROQ_API_KEY

def auto_evaluate(qa_chain, test_questions):
    """
    Automatically evaluates QA outputs using an LLM grader.
    """
    llm = ChatGroq(model=LLM_MODEL, api_key=GROQ_API_KEY)
    eval_chain = QAEvalChain.from_llm(llm)

    examples = [{"query": q, "answer": "Refer to LangChain docs"} for q in test_questions]
    predictions = [qa_chain.run(q) for q in test_questions]

    graded = eval_chain.evaluate(examples=examples, predictions=predictions)
    return graded

if __name__ == "__main__":
    test_qs = [
        "What is an agent in LangChain?",
        "How do I install LangChain?",
        "What’s the role of memory in LangGraph?"
    ]
    # assume qa_chain already built
    results = auto_evaluate(qa_chain, test_qs)
    for r in results:
        print(r)
