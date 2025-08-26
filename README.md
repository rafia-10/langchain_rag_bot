
#LangChain Docs Bot
##Purpose

The LangChain Docs Bot is a technical assistant designed to answer developer questions using the official LangChain documentation. It provides accurate guidance on concepts like Agents, Chains, Memory, Tools, and Retrievers, along with practical how-to instructions and installation guidance.

This project demonstrates how to build a knowledge-based assistant using a focused set of LangChain docs as the knowledge source.

Methodology

Document Selection:

Only official LangChain documentation is used.

Key topics include Introduction, Concepts, Agents, Tools, Retrievers, Tutorials, and How-To guides.

Document Loading:

Web pages are loaded using WebBaseLoader from LangChain.

Only a curated set of URLs (8–25 pages) are used to keep the knowledge base focused.

Cleaning & Preprocessing:

Extra navigation and boilerplate text are removed.

Each document is chunked into manageable pieces (e.g., 800 tokens with 50-token overlap) for embeddings.

Embedding & Storage:

Chunks are embedded using a language model embedding (e.g., OpenAI text-embedding-3-small).

Stored in a vector database (Chroma, FAISS, etc.) for retrieval.

Query Handling:

User queries are processed by a retrieval-augmented generation (RAG) workflow.

Relevant document chunks are retrieved and provided as context for the LLM to answer questions accurately.

Prerequisites

Python 3.10 or higher

Pip package manager

Access to an OpenAI API key (if using OpenAI embeddings)

Internet connection for loading LangChain docs

Installation

Clone the repository:
