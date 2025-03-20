import streamlit as st
import sys
import os

# Add the parent directory to sys.path to allow importing from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.utils import create_new_tab_button

def intro_tab():
    """Display the introduction and setup guide for Archon"""    
    # Welcome message
    st.markdown("""
    Archon is an AI meta-agent designed to autonomously build, refine, and optimize other AI agents.
    
    It serves both as a practical tool for developers and as an educational framework demonstrating the evolution of agentic systems.
    Archon is developed in iterations, starting with a simple Pydantic AI agent that can build other Pydantic AI agents,
    all the way to a full agentic workflow using LangGraph that can build other AI agents with any framework.
    
    Through its iterative development, Archon showcases the power of planning, feedback loops, and domain-specific knowledge in creating robust AI agents.
    """)
    
    # Environment variables update notice
    st.warning("""
    **🔄 IMPORTANT UPDATE (March 13th)**: The environment variables system has been completely overhauled to be more intuitive with separate sections for LLM and Embedding providers. You will need to reset your environment variables in the UI. The new system makes it much easier to switch between different providers and manage profiles as well!
    """)
    
    # Setup guide with expandable sections
    st.markdown("## Setup Guide")
    st.markdown("Follow these concise steps to get Archon up and running (IMPORTANT: come back here after each step):")
    
    # Step 1: Environment Configuration
    with st.expander("Step 1: Environment Configuration", expanded=True):
        st.markdown("""
        ### Environment Configuration
        
        First, you need to set up your environment variables:
        
        1. Go to the **Environment** tab
        2. Configure the following essential variables:
           - `BASE_URL`: API endpoint (OpenAI, OpenRouter, or Ollama)
           - `LLM_API_KEY`: Your API key for the LLM service
           - `OPENAI_API_KEY`: Required for embeddings
           - `SUPABASE_URL`: Your Supabase project URL
           - `SUPABASE_SERVICE_KEY`: Your Supabase service key
           - `PRIMARY_MODEL`: Main agent model (e.g., gpt-4o-mini)
           - `REASONER_MODEL`: Planning model (e.g., o3-mini)
        
        These settings determine how Archon connects to external services and which models it uses.
        """)
        # Add a button to navigate to the Environment tab
        create_new_tab_button("Go to Environment Section (New Tab)", "Environment", key="goto_env", use_container_width=True)
    
    # Step 2: Database Setup
    with st.expander("Step 2: Database Setup", expanded=False):
        st.markdown("""
        ### Database Setup
        
        Archon uses Supabase for vector storage and retrieval:
        
        1. Go to the **Database** tab
        2. Select your embedding dimensions (1536 for OpenAI, 768 for nomic-embed-text)
        3. Follow the instructions to create the `site_pages` table
        
        This creates the necessary tables, indexes, and functions for vector similarity search.
        """)
        # Add a button to navigate to the Database tab
        create_new_tab_button("Go to Database Section (New Tab)", "Database", key="goto_db", use_container_width=True)
    
    # Step 3: Documentation Crawling
    with st.expander("Step 3: Documentation Crawling", expanded=False):
        st.markdown("""
        ### Documentation Crawling
        
        Populate the database with framework documentation:
        
        1. Go to the **Documentation** tab
        2. Click on "Crawl Pydantic AI Docs"
        3. Wait for the crawling process to complete
        
        This step downloads and processes documentation, creating embeddings for semantic search.
        """)
        # Add a button to navigate to the Documentation tab
        create_new_tab_button("Go to the Documentation Section (New Tab)", "Documentation", key="goto_docs", use_container_width=True)
    
    # Step 4: Agent Service
    with st.expander("Step 4: Agent Service Setup (for MCP)", expanded=False):
        st.markdown("""
        ### MCP Agent Service Setup
        
        Start the graph service for agent generation:
        
        1. Go to the **Agent Service** tab
        2. Click on "Start Agent Service"
        3. Verify the service is running
        
        The agent service powers the LangGraph workflow for agent creation.
        """)
        # Add a button to navigate to the Agent Service tab
        create_new_tab_button("Go to Agent Service Section (New Tab)", "Agent Service", key="goto_service", use_container_width=True)
    
    # Step 5: MCP Configuration (Optional)
    with st.expander("Step 5: MCP Configuration (Optional)", expanded=False):
        st.markdown("""
        ### MCP Configuration
        
        For integration with AI IDEs:
        
        1. Go to the **MCP** tab
        2. Select your IDE (Windsurf, Cursor, or Cline/Roo Code)
        3. Follow the instructions to configure your IDE
        
        This enables you to use Archon directly from your AI-powered IDE.
        """)
        # Add a button to navigate to the MCP tab
        create_new_tab_button("Go to MCP Section (New Tab)", "MCP", key="goto_mcp", use_container_width=True)
    
    # Step 6: Using Archon
    with st.expander("Step 6: Using Archon", expanded=False):
        st.markdown("""
        ### Using Archon
        
        Once everything is set up:
        
        1. Go to the **Chat** tab
        2. Describe the agent you want to build
        3. Archon will plan and generate the necessary code
        
        You can also use Archon directly from your AI IDE if you've configured MCP.
        """)
        # Add a button to navigate to the Chat tab
        create_new_tab_button("Go to Chat Section (New Tab)", "Chat", key="goto_chat", use_container_width=True)
    
    # Resources
    st.markdown("""
    ## Additional Resources
    
    - [GitHub Repository](https://github.com/coleam00/archon)
    - [Archon Community Forum](https://thinktank.ottomator.ai/c/archon/30)
    - [GitHub Kanban Board](https://github.com/users/coleam00/projects/1)
    """)