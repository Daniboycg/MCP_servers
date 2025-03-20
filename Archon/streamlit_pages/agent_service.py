import streamlit as st
import subprocess
import threading
import platform
import queue
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.utils import reload_archon_graph

def agent_service_tab():
    """Display the agent service interface for managing the graph service"""
    st.header("MCP Agent Service")
    st.write("Start, restart, and monitor the Archon agent service for MCP.")
    
    # Initialize session state variables if they don't exist
    if "service_process" not in st.session_state:
        st.session_state.service_process = None
    if "service_running" not in st.session_state:
        st.session_state.service_running = False
    if "service_output" not in st.session_state:
        st.session_state.service_output = []
    if "output_queue" not in st.session_state:
        st.session_state.output_queue = queue.Queue()
    
    # Function to check if the service is running
    def is_service_running():
        if st.session_state.service_process is None:
            return False
        
        # Check if process is still running
        return st.session_state.service_process.poll() is None
    
    # Function to kill any process using port 8100
    def kill_process_on_port(port):
        try:
            if platform.system() == "Windows":
                # Windows: use netstat to find the process using the port
                result = subprocess.run(
                    f'netstat -ano | findstr :{port}',
                    shell=True, 
                    capture_output=True, 
                    text=True
                )
                
                if result.stdout:
                    # Extract the PID from the output
                    for line in result.stdout.splitlines():
                        if f":{port}" in line and "LISTENING" in line:
                            parts = line.strip().split()
                            pid = parts[-1]
                            # Kill the process
                            subprocess.run(f'taskkill /F /PID {pid}', shell=True)
                            st.session_state.output_queue.put(f"[{time.strftime('%H:%M:%S')}] Killed any existing process using port {port} (PID: {pid})\n")
                            return True
            else:
                # Unix-like systems: use lsof to find the process using the port
                result = subprocess.run(
                    f'lsof -i :{port} -t',
                    shell=True, 
                    capture_output=True, 
                    text=True
                )
                
                if result.stdout:
                    # Extract the PID from the output
                    pid = result.stdout.strip()
                    # Kill the process
                    subprocess.run(f'kill -9 {pid}', shell=True)
                    st.session_state.output_queue.put(f"[{time.strftime('%H:%M:%S')}] Killed process using port {port} (PID: {pid})\n")
                    return True
                    
            return False
        except Exception as e:
            st.session_state.output_queue.put(f"[{time.strftime('%H:%M:%S')}] Error killing process on port {port}: {str(e)}\n")
            return False
    
    # Update service status
    st.session_state.service_running = is_service_running()
    
    # Process any new output in the queue
    try:
        while not st.session_state.output_queue.empty():
            line = st.session_state.output_queue.get_nowait()
            if line:
                st.session_state.service_output.append(line)
    except Exception:
        pass
    
    # Create button text based on service status
    button_text = "Restart Agent Service" if st.session_state.service_running else "Start Agent Service"
    
    # Create columns for buttons
    col1, col2 = st.columns([1, 1])
    
    # Start/Restart button
    with col1:
        if st.button(button_text, use_container_width=True):
            # Stop existing process if running
            if st.session_state.service_running:
                try:
                    st.session_state.service_process.terminate()
                    time.sleep(1)  # Give it time to terminate
                    if st.session_state.service_process.poll() is None:
                        # Force kill if still running
                        st.session_state.service_process.kill()
                except Exception as e:
                    st.error(f"Error stopping service: {str(e)}")
            
            # Clear previous output
            st.session_state.service_output = []
            st.session_state.output_queue = queue.Queue()
            
            # Kill any process using port 8100
            kill_process_on_port(8100)
            
            # Start new process
            try:
                # Get the absolute path to the graph service script
                base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
                graph_service_path = os.path.join(base_path, 'graph_service.py')
                
                # Start the process with output redirection
                process = subprocess.Popen(
                    [sys.executable, graph_service_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                
                st.session_state.service_process = process
                st.session_state.service_running = True
                
                # Start threads to read output
                def read_output(stream, queue_obj):
                    for line in iter(stream.readline, ''):
                        queue_obj.put(line)
                    stream.close()
                
                # Start threads for stdout and stderr
                threading.Thread(target=read_output, args=(process.stdout, st.session_state.output_queue), daemon=True).start()
                threading.Thread(target=read_output, args=(process.stderr, st.session_state.output_queue), daemon=True).start()
                
                # Add startup message
                st.session_state.output_queue.put(f"[{time.strftime('%H:%M:%S')}] Agent service started\n")
                
                st.success("Agent service started successfully!")
                st.rerun()
                
            except Exception as e:
                st.error(f"Error starting service: {str(e)}")
                st.session_state.output_queue.put(f"[{time.strftime('%H:%M:%S')}] Error: {str(e)}\n")
    
    # Stop button
    with col2:
        stop_button = st.button("Stop Agent Service", disabled=not st.session_state.service_running, use_container_width=True)
        if stop_button and st.session_state.service_running:
            try:
                st.session_state.service_process.terminate()
                time.sleep(1)  # Give it time to terminate
                if st.session_state.service_process.poll() is None:
                    # Force kill if still running
                    st.session_state.service_process.kill()
                
                st.session_state.service_running = False
                st.session_state.output_queue.put(f"[{time.strftime('%H:%M:%S')}] Agent service stopped\n")
                st.success("Agent service stopped successfully!")
                st.rerun()
                
            except Exception as e:
                st.error(f"Error stopping service: {str(e)}")
                st.session_state.output_queue.put(f"[{time.strftime('%H:%M:%S')}] Error stopping: {str(e)}\n")
    
    # Service status indicator
    status_color = "🟢" if st.session_state.service_running else "🔴"
    status_text = "Running" if st.session_state.service_running else "Stopped"
    st.write(f"**Service Status:** {status_color} {status_text}")
    
    # Add auto-refresh option
    auto_refresh = st.checkbox("Auto-refresh output (uncheck this before copying any error message)", value=True)
    
    # Display output in a scrollable container
    st.subheader("Service Output")
    
    # Calculate height based on number of lines, but cap it
    output_height = min(400, max(200, len(st.session_state.service_output) * 20))
    
    # Create a scrollable container for the output
    with st.container():
        # Join all output lines and display in the container
        output_text = "".join(st.session_state.service_output)
        
        # For auto-scrolling, we'll use a different approach
        if auto_refresh and st.session_state.service_running and output_text:
            # We'll reverse the output text so the newest lines appear at the top
            # This way they're always visible without needing to scroll
            lines = output_text.splitlines()
            reversed_lines = lines[::-1]  # Reverse the lines
            output_text = "\n".join(reversed_lines)
            
            # Add a note at the top (which will appear at the bottom of the reversed text)
            note = "--- SHOWING NEWEST LOGS FIRST (AUTO-SCROLL MODE) ---\n\n"
            output_text = note + output_text
        
        # Use a text area for scrollable output
        st.text_area(
            label="Realtime Logs from Archon Service",
            value=output_text,
            height=output_height,
            disabled=True,
            key="output_text_area"  # Use a fixed key to maintain state between refreshes
        )
        
        # Add a toggle for reversed mode
        if auto_refresh and st.session_state.service_running:
            st.caption("Logs are shown newest-first for auto-scrolling. Disable auto-refresh to see logs in chronological order.")
    
    # Add a clear output button
    if st.button("Clear Output"):
        st.session_state.service_output = []
        st.rerun()
    
    # Auto-refresh if enabled and service is running
    if auto_refresh and st.session_state.service_running:
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage
        st.rerun()