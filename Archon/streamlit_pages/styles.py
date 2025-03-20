"""
This module contains the CSS styles for the Streamlit UI.
"""

import streamlit as st

def load_css():
    """
    Load the custom CSS styles for the Archon UI.
    """
    st.markdown("""
        <style>
        :root {
            --primary-color: #00CC99;  /* Green */
            --secondary-color: #EB2D8C; /* Pink */
            --text-color: #262730;
        }
        
        /* Style the buttons */
        .stButton > button {
            color: white;
            border: 2px solid var(--primary-color);
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            color: white;
            border: 2px solid var(--secondary-color);
        }
        
        /* Override Streamlit's default focus styles that make buttons red */
        .stButton > button:focus, 
        .stButton > button:focus:hover, 
        .stButton > button:active, 
        .stButton > button:active:hover {
            color: white !important;
            border: 2px solid var(--secondary-color) !important;
            box-shadow: none !important;
            outline: none !important;
        }
        
        /* Style headers */
        h1, h2, h3 {
            color: var(--primary-color);
        }
        
        /* Hide spans within h3 elements */
        h1 span, h2 span, h3 span {
            display: none !important;
            visibility: hidden;
            width: 0;
            height: 0;
            opacity: 0;
            position: absolute;
            overflow: hidden;
        }
        
        /* Style code blocks */
        pre {
            border-left: 4px solid var(--primary-color);
        }
        
        /* Style links */
        a {
            color: var(--secondary-color);
        }
        
        /* Style the chat messages */
        .stChatMessage {
            border-left: 4px solid var(--secondary-color);
        }
        
        /* Style the chat input */
        .stChatInput > div {
            border: 2px solid var(--primary-color) !important;
        }
        
        /* Remove red outline on focus */
        .stChatInput > div:focus-within {
            box-shadow: none !important;
            border: 2px solid var(--secondary-color) !important;
            outline: none !important;
        }
        
        /* Remove red outline on all inputs when focused */
        input:focus, textarea:focus, [contenteditable]:focus {
            box-shadow: none !important;
            border-color: var(--secondary-color) !important;
            outline: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
