# Archon V4 - Streamlit UI Overhaul (and Docker Support)

This is the fourth iteration of the Archon project, building upon V3 by adding a comprehensive Streamlit UI for managing all aspects of Archon and Docker support. The system retains the core LangGraph workflow and MCP support from V3, but now provides a unified interface for environment configuration, database setup, documentation crawling, agent service management, and MCP integration.

What makes V4 special is its guided setup process that walks users through each step of configuring and running Archon. The Streamlit UI eliminates the need for manual configuration of environment variables, database setup, and service management, making Archon much more accessible to users without extensive technical knowledge.

The core remains an intelligent documentation crawler and RAG (Retrieval-Augmented Generation) system built using Pydantic AI, LangGraph, and Supabase. The system crawls the Pydantic AI documentation, stores content in a vector database, and provides Pydantic AI agent code by retrieving and analyzing relevant documentation chunks.

This version continues to support both local LLMs with Ollama and cloud-based LLMs through OpenAI/OpenRouter.

## Key Features

- **Comprehensive Streamlit UI**: Unified interface for all Archon functionality
- **Docker Support**: Containerized deployment with automated build and run scripts
- **Guided Setup Process**: Step-by-step instructions for configuration
- **Environment Variable Management**: Configure all settings through the UI
- **Database Setup**: Automated creation of Supabase tables and indexes
- **Documentation Crawler**: Fetch and process documentation for RAG
- **Agent Service Management**: Start/stop the agent service from the UI
- **MCP Integration**: Configure and manage MCP for AI IDE integration
- **Multiple LLM Support**: OpenAI, OpenRouter, and local Ollama models
- **Multi-agent workflow using LangGraph**: Manage multiple agents simultaneously

## Prerequisites
- Docker (optional but preferred)
- Python 3.11+
- Supabase account (for vector database)
- OpenAI/OpenRouter/Anthropic API key or Ollama for local LLMs

## Installation

### Option 1: Docker (Recommended)
1. Clone the repository:
```bash
git clone https://github.com/coleam00/archon.git
cd archon/iterations/v4-streamlit-ui-overhaul
```

2. Run the Docker setup script:
```bash
# This will build both containers and start Archon
python run_docker.py
```

3. Access the Streamlit UI at http://localhost:8501.

> **Note:** `run_docker.py` will automatically:
> - Build the MCP server container
> - Build the main Archon container
> - Run Archon with the appropriate port mappings
> - Use environment variables from `.env` file if it exists

### Option 2: Local Python Installation
1. Clone the repository:
```bash
git clone https://github.com/coleam00/archon.git
cd archon/iterations/v4-streamlit-ui-overhaul
```

2. Install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Start the Streamlit UI:
```bash
streamlit run streamlit_ui.py
```

4. Access the Streamlit UI at http://localhost:8501.

### Streamlit UI Tabs

The Streamlit interface will guide you through each step with clear instructions and interactive elements.
There are a good amount of steps for the setup but it goes quick!

The Streamlit UI provides the following tabs:

1. **Intro**: Overview and guided setup process
2. **Environment**: Configure API keys and model settings
3. **Database**: Set up your Supabase vector database
4. **Documentation**: Crawl and index the Pydantic AI documentation
5. **Agent Service**: Start and monitor the agent service
6. **Chat**: Interact with Archon to create AI agents
7. **MCP**: Configure integration with AI IDEs

### Environment Configuration

The Environment tab allows you to set and manage all environment variables through the UI:

- Base URL for API endpoints
- API keys for LLM providers
- Supabase connection details
- Model selections for different agent roles
- Embedding model configuration

All settings are saved to an `env_vars.json` file, which is automatically loaded when Archon starts.

### Database Setup

The Database tab simplifies the process of setting up your Supabase database:

- Select embedding dimensions based on your model
- View SQL commands for table creation
- Get instructions for executing SQL in Supabase
- Clear existing data if needed

### Documentation Management

The Documentation tab provides an interface for crawling and managing documentation:

- Start and monitor the crawling process with progress tracking
- View logs of the crawling process
- Clear existing documentation
- View database statistics

### Agent Service Control

The Agent Service tab allows you to manage the agent service:

- Start, restart, and stop the service
- Monitor service output in real-time
- Clear output logs
- Auto-refresh for continuous monitoring

### MCP Configuration

The MCP tab simplifies the process of configuring MCP for AI IDEs:

- Select your IDE (Windsurf, Cursor, Cline, or Roo Code)
- Generate configuration commands or JSON
- Copy configuration to clipboard
- Get step-by-step instructions for your specific IDE

## Architecture

### Core Files
- `streamlit_ui.py`: Comprehensive web interface for managing all aspects of Archon
- `graph_service.py`: FastAPI service that handles the agentic workflow
- `run_docker.py`: Script to build and run Archon Docker containers
- `Dockerfile`: Container definition for the main Archon application

### MCP Integration
- `mcp/`: Model Context Protocol server implementation
  - `mcp_server.py`: MCP server script for AI IDE integration
  - `Dockerfile`: Container definition for the MCP server

### Archon Package
- `archon/`: Core agent and workflow implementation
  - `archon_graph.py`: LangGraph workflow definition and agent coordination
  - `pydantic_ai_coder.py`: Main coding agent with RAG capabilities
  - `crawl_pydantic_ai_docs.py`: Documentation crawler and processor

### Utilities
- `utils/`: Utility functions and database setup
  - `utils.py`: Shared utility functions
  - `site_pages.sql`: Database setup commands
  - `env_vars.json`: Environment variables defined in the UI are stored here (included in .gitignore, file is created automatically)

## Deployment Options
- **Docker Containers**: Run Archon in isolated containers with all dependencies included
  - Main container: Runs the Streamlit UI and graph service
  - MCP container: Provides MCP server functionality for AI IDEs
- **Local Python**: Run directly on your system with a Python virtual environment

### Docker Architecture
The Docker implementation consists of two containers:
1. **Main Archon Container**:
   - Runs the Streamlit UI on port 8501
   - Hosts the Graph Service on port 8100
   - Built from the root Dockerfile
   - Handles all agent functionality and user interactions

2. **MCP Container**:
   - Implements the Model Context Protocol for AI IDE integration
   - Built from the mcp/Dockerfile
   - Communicates with the main container's Graph Service
   - Provides a standardized interface for AI IDEs like Windsurf, Cursor, Cline and Roo Code

When running with Docker, the `run_docker.py` script automates building and starting both containers with the proper configuration.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
