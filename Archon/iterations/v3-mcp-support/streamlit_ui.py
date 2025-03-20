from __future__ import annotations
from typing import Literal, TypedDict
from langgraph.types import Command
from openai import AsyncOpenAI
from supabase import Client
import streamlit as st
import logfire
import asyncio
import json
import uuid
import os
import sys

# Import all the message part classes
from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    SystemPromptPart,
    UserPromptPart,
    TextPart,
    ToolCallPart,
    ToolReturnPart,
    RetryPromptPart,
    ModelMessagesTypeAdapter
)

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from archon.archon_graph import agentic_flow

# Load environment variables
from dotenv import load_dotenv
load_dotenv()


openai_client=None
base_url = os.getenv('BASE_URL', 'https://api.openai.com/v1')
api_key = os.getenv('LLM_API_KEY', 'no-llm-api-key-provided')
is_ollama = "localhost" in base_url.lower()

if is_ollama:
    openai_client = AsyncOpenAI(base_url=base_url,api_key=api_key)
else:
    openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

supabase: Client = Client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

# Configure logfire to suppress warnings (optional)
logfire.configure(send_to_logfire='never')

@st.cache_resource
def get_thread_id():
    return str(uuid.uuid4())

thread_id = get_thread_id()

async def run_agent_with_streaming(user_input: str):
    """
    Run the agent with streaming text for the user_input prompt,
    while maintaining the entire conversation in `st.session_state.messages`.
    """
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    # First message from user
    if len(st.session_state.messages) == 1:
        async for msg in agentic_flow.astream(
                {"latest_user_message": user_input}, config, stream_mode="custom"
            ):
                yield msg
    # Continue the conversation
    else:
        async for msg in agentic_flow.astream(
            Command(resume=user_input), config, stream_mode="custom"
        ):
            yield msg


async def main():
    st.title("Archon - Agent Builder")
    st.write("Describe to me an AI agent you want to build and I'll code it for you with Pydantic AI.")
    st.write("Example: Build me an AI agent that can search the web with the Brave API.")

    # Initialize chat history in session state if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        message_type = message["type"]
        if message_type in ["human", "ai", "system"]:
            with st.chat_message(message_type):
                st.markdown(message["content"])    

    # Chat input for the user
    user_input = st.chat_input("What do you want to build today?")

    if user_input:
        # We append a new request to the conversation explicitly
        st.session_state.messages.append({"type": "human", "content": user_input})
        
        # Display user prompt in the UI
        with st.chat_message("user"):
            st.markdown(user_input)

        # Display assistant response in chat message container
        response_content = ""
        with st.chat_message("assistant"):
            message_placeholder = st.empty()  # Placeholder for updating the message
            # Run the async generator to fetch responses
            async for chunk in run_agent_with_streaming(user_input):
                response_content += chunk
                # Update the placeholder with the current response content
                message_placeholder.markdown(response_content)
        
        st.session_state.messages.append({"type": "ai", "content": response_content})


if __name__ == "__main__":
    asyncio.run(main())
