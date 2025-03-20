# Archon V2 - Agentic Workflow for Building Pydantic AI Agents

This is the second iteration of the Archon project, building upon V1 by introducing LangGraph for a full agentic workflow. The system starts with a reasoning LLM (like O3-mini or R1) that analyzes user requirements and documentation to create a detailed scope, which then guides specialized coding and routing agents in generating high-quality Pydantic AI agents.

An intelligent documentation crawler and RAG (Retrieval-Augmented Generation) system built using Pydantic AI, LangGraph, and Supabase that is capable of building other Pydantic AI agents. The system crawls the Pydantic AI documentation, stores content in a vector database, and provides Pydantic AI agent code by retrieving and analyzing relevant documentation chunks.

This version also supports local LLMs with Ollama for the main agent and reasoning LLM.

Note that we are still relying on OpenAI for embeddings no matter what, but future versions of Archon will change that.

## Features

- Multi-agent workflow using LangGraph
- Specialized agents for reasoning, routing, and coding
- Pydantic AI documentation crawling and chunking
- Vector database storage with Supabase
- Semantic search using OpenAI embeddings
- RAG-based question answering
- Support for code block preservation
- Streamlit UI for interactive querying

## Prerequisites

- Python 3.11+
- Supabase account and database
- OpenAI/OpenRouter API key or Ollama for local LLMs
- Streamlit (for web interface)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/coleam00/archon.git
cd archon/iterations/v2-agentic-workflow
```

2. Install dependencies (recommended to use a Python virtual environment):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up environment variables:
   - Rename `.env.example` to `.env`
   - Edit `.env` with your API keys and preferences:
   ```env
   BASE_URL=https://api.openai.com/v1 for OpenAI, https://api.openrouter.ai/v1 for OpenRouter, or your Ollama URL
   LLM_API_KEY=your_openai_or_openrouter_api_key
   OPENAI_API_KEY=your_openai_api_key
   SUPABASE_URL=your_supabase_url
   SUPABASE_SERVICE_KEY=your_supabase_service_key
   PRIMARY_MODEL=gpt-4o-mini  # or your preferred OpenAI model for main agent
   REASONER_MODEL=o3-mini     # or your preferred OpenAI model for reasoning
   ```

## Usage

### Database Setup

Execute the SQL commands in `site_pages.sql` to:
1. Create the necessary tables
2. Enable vector similarity search
3. Set up Row Level Security policies

In Supabase, do this by going to the "SQL Editor" tab and pasting in the SQL into the editor there. Then click "Run".

### Crawl Documentation

To crawl and store documentation in the vector database:

```bash
python crawl_pydantic_ai_docs.py
```

This will:
1. Fetch URLs from the documentation sitemap
2. Crawl each page and split into chunks
3. Generate embeddings and store in Supabase

### Chunking Configuration

You can configure chunking parameters in `crawl_pydantic_ai_docs.py`:
```python
chunk_size = 5000  # Characters per chunk
```

The chunker intelligently preserves:
- Code blocks
- Paragraph boundaries
- Sentence boundaries

### Streamlit Web Interface

For an interactive web interface to query the documentation and create agents:

```bash
streamlit run streamlit_ui.py
```

The interface will be available at `http://localhost:8501`

## Configuration

### Database Schema

The Supabase database uses the following schema:
```sql
CREATE TABLE site_pages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    url TEXT,
    chunk_number INTEGER,
    title TEXT,
    summary TEXT,
    content TEXT,
    metadata JSONB,
    embedding VECTOR(1536)
);
```

## Project Structure

- `archon_graph.py`: LangGraph workflow definition and agent coordination
- `pydantic_ai_coder.py`: Main coding agent with RAG capabilities
- `crawl_pydantic_ai_docs.py`: Documentation crawler and processor
- `streamlit_ui.py`: Web interface with streaming support
- `site_pages.sql`: Database setup commands
- `requirements.txt`: Project dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
