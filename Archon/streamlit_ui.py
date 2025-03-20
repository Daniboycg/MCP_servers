from __future__ import annotations
from dotenv import load_dotenv
import streamlit as st
import logfire
import asyncio

# Set page config - must be the first Streamlit command
st.set_page_config(
    page_title="Archon - Agent Builder",
    page_icon="🤖",
    layout="wide",
)

# Utilities and styles
from utils.utils import get_clients
from streamlit_pages.styles import load_css

# Streamlit pages
from streamlit_pages.intro import intro_tab
from streamlit_pages.chat import chat_tab
from streamlit_pages.environment import environment_tab
from streamlit_pages.database import database_tab
from streamlit_pages.documentation import documentation_tab
from streamlit_pages.agent_service import agent_service_tab
from streamlit_pages.mcp import mcp_tab
from streamlit_pages.future_enhancements import future_enhancements_tab

# Load environment variables from .env file
load_dotenv()

# Initialize clients
openai_client, supabase = get_clients()

# Load custom CSS styles
load_css()

# Configure logfire to suppress warnings (optional)
logfire.configure(send_to_logfire='never')

async def main():
    # Check for tab query parameter
    query_params = st.query_params
    if "tab" in query_params:
        tab_name = query_params["tab"]
        if tab_name in ["Intro", "Chat", "Environment", "Database", "Documentation", "Agent Service", "MCP", "Future Enhancements"]:
            st.session_state.selected_tab = tab_name

    # Add sidebar navigation
    with st.sidebar:
        st.image("public/ArchonLightGrey.png", width=1000)
        
        # Navigation options with vertical buttons
        st.write("### Navigation")
        
        # Initialize session state for selected tab if not present
        if "selected_tab" not in st.session_state:
            st.session_state.selected_tab = "Intro"
        
        # Vertical navigation buttons
        intro_button = st.button("Intro", use_container_width=True, key="intro_button")
        chat_button = st.button("Chat", use_container_width=True, key="chat_button")
        env_button = st.button("Environment", use_container_width=True, key="env_button")
        db_button = st.button("Database", use_container_width=True, key="db_button")
        docs_button = st.button("Documentation", use_container_width=True, key="docs_button")
        service_button = st.button("Agent Service", use_container_width=True, key="service_button")
        mcp_button = st.button("MCP", use_container_width=True, key="mcp_button")
        future_enhancements_button = st.button("Future Enhancements", use_container_width=True, key="future_enhancements_button")
        
        # Update selected tab based on button clicks
        if intro_button:
            st.session_state.selected_tab = "Intro"
        elif chat_button:
            st.session_state.selected_tab = "Chat"
        elif mcp_button:
            st.session_state.selected_tab = "MCP"
        elif env_button:
            st.session_state.selected_tab = "Environment"
        elif service_button:
            st.session_state.selected_tab = "Agent Service"
        elif db_button:
            st.session_state.selected_tab = "Database"
        elif docs_button:
            st.session_state.selected_tab = "Documentation"
        elif future_enhancements_button:
            st.session_state.selected_tab = "Future Enhancements"
    
    # Display the selected tab
    if st.session_state.selected_tab == "Intro":
        st.title("Archon - Introduction")
        intro_tab()
    elif st.session_state.selected_tab == "Chat":
        st.title("Archon - Agent Builder")
        await chat_tab()
    elif st.session_state.selected_tab == "MCP":
        st.title("Archon - MCP Configuration")
        mcp_tab()
    elif st.session_state.selected_tab == "Environment":
        st.title("Archon - Environment Configuration")
        environment_tab()
    elif st.session_state.selected_tab == "Agent Service":
        st.title("Archon - Agent Service")
        agent_service_tab()
    elif st.session_state.selected_tab == "Database":
        st.title("Archon - Database Configuration")
        database_tab(supabase)
    elif st.session_state.selected_tab == "Documentation":
        st.title("Archon - Documentation")
        documentation_tab(supabase)
    elif st.session_state.selected_tab == "Future Enhancements":
        st.title("Archon - Future Enhancements")
        future_enhancements_tab()

if __name__ == "__main__":
    asyncio.run(main())
