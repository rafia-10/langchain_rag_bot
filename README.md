🚀 LangChain Docs Bot

A developer assistant that answers questions using official LangChain documentation.

Perfect for understanding Agents, Chains, Memory, Tools, Retrievers, and more, with practical examples and how-to guides.

🎯 Purpose

LangChain Docs Bot helps developers quickly find accurate answers about LangChain concepts and usage.

Uses official LangChain docs as a trusted knowledge source

Answers questions on core concepts, tutorials, tools, and installation

Demonstrates a knowledge-based RAG workflow

🧠 Methodology

Document Selection

Only official LangChain documentation

Focused topics: Introduction, Concepts, Agents, Tools, Retrievers, Tutorials, How-To

Loading Documents

Load pages using WebBaseLoader

Curated 8–25 URLs for a compact, high-value knowledge base

Cleaning & Chunking

Remove navigation/boilerplate text

Chunk documents: chunk_size=800, chunk_overlap=50

Embedding & Storage

Embed chunks using OpenAI or compatible embeddings

Store in a vector database (Chroma, FAISS, etc.) for fast retrieval

Query Handling

User questions trigger retrieval of relevant chunks

LLM generates accurate, context-aware answers

⚙️ Prerequisites

Python 3.10+

Pip package manager

Internet access

OpenAI API key (if using OpenAI embeddings)

🛠️ Installation
