# 📚 LangChain RAG Bot

A lightweight Retrieval-Augmented Generation (RAG) bot built on LangChain docs.
This assistant can answer technical questions such as:

“How do I define a custom agent in LangChain?”

“What’s the role of memory in LangGraph?”

It uses:

HuggingFace embeddings for semantic understanding

ChromaDB as a vector store with cosine similarity

Groq LLM (LLaMA-3) for fast, accurate responses

## ✨ Purpose

The project demonstrates how to build a domain-specific knowledge assistant using only LangChain’s official documentation (20–50 curated pages).
This keeps the knowledge base focused, efficient, and evaluator-friendly.

## ⚙️ Methodology

Load Docs → Fetch LangChain documentation pages.

Clean & Chunk → Split docs into overlapping chunks for context.

Embed Text → Use HuggingFace all-MiniLM-L6-v2 for embeddings.

Store in Vector DB → Save embeddings in ChromaDB (cosine similarity).

Retrieve Relevant Chunks → Query vector DB for relevant sections.

Generate Answer → Use Groq’s LLaMA-3 model with RAG context.

## 📋 Prerequisites

Python 3.9+

Virtual environment (venv) recommended

Groq API key (free)

## 🛠 Installation

#### 1️⃣ Clone the repo

git clone https://github.com/your-username/langchain-rag-bot.git
cd langchain-rag-bot

#### 2️⃣ Create & activate virtual environment

python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

#### 3️⃣ Install dependencies

pip install -r requirements.txt

## 🔑 Environment Setup

create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

## 🚀 Usage
Run the bot from the project root:

python main.py

### You can then ask questions like:
❓ What are LangChain agents?
❓ How do retrievers work?
❓ How do I install LangChain?

### The bot will:

Retrieve the most relevant chunks from docs

Generate an accurate answer with sources


## 🧩 Project Structure

langchain_rag_bot/
│── config.py         # Configuration & constants
│── data_loader.py    # Load & clean LangChain docs
│── vectorstore.py    # Store/retrieve from ChromaDB
│── llm.py            # Groq LLM integration
│── main.py           # Entry point
│── requirements.txt  # Dependencies
│── .env.example      # Example env file

## 📝 Example Query

Q: How do I define a custom agent in LangChain?  

AI Answer:  
Custom agents are built by ... (generated answer here)

Sources:  
- concepts/agents/  
- concepts/tools/  

## ⚡ Tech Stack

LangChain
ChromaDB
HuggingFace Sentence-Transformers
Groq LLaMA-3


## 📌 Notes for Evaluators

Knowledge base limited to 8 LangChain doc pages (within 20–50 page scope).

Uses cosine similarity for retrieval.

No paid services — HuggingFace (free embeddings) + Groq (free API key).

## 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.


