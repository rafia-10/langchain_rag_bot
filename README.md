📚 LangChain RAG Bot

A lightweight Retrieval-Augmented Generation (RAG) bot built on LangChain docs.
This assistant can answer technical questions such as:

“How do I define a custom agent in LangChain?”

“What’s the role of memory in LangGraph?”

It uses:

HuggingFace embeddings for semantic understanding

ChromaDB as a vector store with cosine similarity

Groq LLM (LLaMA-3) for fast, accurate responses

✨ Purpose

The project demonstrates how to build a domain-specific knowledge assistant using only LangChain’s official documentation (20–50 curated pages).
This keeps the knowledge base focused, efficient, and evaluator-friendly.

⚙️ Methodology

Load Docs → Fetch LangChain documentation pages.

Clean & Chunk → Split docs into overlapping chunks for context.

Embed Text → Use HuggingFace all-MiniLM-L6-v2 for embeddings.

Store in Vector DB → Save embeddings in ChromaDB (cosine similarity).

Retrieve Relevant Chunks → Query vector DB for relevant sections.

Generate Answer → Use Groq’s LLaMA-3 model with RAG context.

📋 Prerequisites

Python 3.9+

Virtual environment (venv) recommended

Groq API key (free)

🛠 Installation
