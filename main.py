from dotenv import load_dotenv
load_dotenv()   

from data_loader import load_docs
from chunker import chunk_docs
from embedder import get_embedder
from vectorstore import build_vectorstore
from qa_chain import build_qa_chain
from query_processor import clean_query, rephrase_query_with_llm


def run_bot():
    # Step 1: Load docs
    docs = load_docs()

    # Step 2: Chunk docs
    chunks = chunk_docs(docs)

    # Step 3: Init embeddings
    embeddings = get_embedder()

    # Step 4: Build vectorstore
    vectorstore = build_vectorstore(chunks, embeddings)

    # Step 5: Setup QA chain
    qa = build_qa_chain(vectorstore)
    while True:
        raw_query = input("\n🤔 Your Question (type 'exit' to quit): ")
        if raw_query.lower() == "exit":
            break

        query = clean_query(raw_query)
        query = rephrase_query_with_llm(query)  # ✅ smarter preprocessing
        # print("⚙️ Final Processed Query:", query)

        answer = qa.run(query)
        print("\n💡 Answer:", answer)


if __name__ == "__main__":
    run_bot()
