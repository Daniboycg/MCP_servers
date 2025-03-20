import os
from datetime import datetime
from functools import wraps
import inspect
import json
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def write_to_log(message: str):
    """Write a message to the logs.txt file in the workbench directory.
    
    Args:
        message: The message to log
    """
    # Get the directory one level up from the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    workbench_dir = os.path.join(parent_dir, "workbench")
    log_path = os.path.join(workbench_dir, "logs.txt")
    os.makedirs(workbench_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_entry)

def get_env_var(var_name: str) -> Optional[str]:
    """Get an environment variable from the saved JSON file or from environment variables.
    
    Args:
        var_name: The name of the environment variable to retrieve
        
    Returns:
        The value of the environment variable or None if not found
    """
    # Path to the JSON file storing environment variables
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    env_file_path = os.path.join(current_dir, "env_vars.json")
    
    # First try to get from JSON file
    if os.path.exists(env_file_path):
        try:
            with open(env_file_path, "r") as f:
                env_vars = json.load(f)
                if var_name in env_vars and env_vars[var_name]:
                    return env_vars[var_name]
        except (json.JSONDecodeError, IOError) as e:
            write_to_log(f"Error reading env_vars.json: {str(e)}")
    
    # If not found in JSON, try to get from environment variables
    return os.environ.get(var_name)

def save_env_var(var_name: str, value: str) -> bool:
    """Save an environment variable to the JSON file.
    
    Args:
        var_name: The name of the environment variable
        value: The value to save
        
    Returns:
        True if successful, False otherwise
    """
    # Path to the JSON file storing environment variables
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.join(current_dir, "env_vars.json")
    
    # Load existing env vars or create empty dict
    env_vars = {}
    if os.path.exists(env_file_path):
        try:
            with open(env_file_path, "r") as f:
                env_vars = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            write_to_log(f"Error reading env_vars.json: {str(e)}")
            # Continue with empty dict if file is corrupted
    
    # Update the variable
    env_vars[var_name] = value
    
    # Save back to file
    try:
        with open(env_file_path, "w") as f:
            json.dump(env_vars, f, indent=2)
        return True
    except IOError as e:
        write_to_log(f"Error writing to env_vars.json: {str(e)}")
        return False

def log_node_execution(func):
    """Decorator to log the start and end of graph node execution.
    
    Args:
        func: The async function to wrap
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        func_name = func.__name__
        write_to_log(f"Starting node: {func_name}")
        try:
            result = await func(*args, **kwargs)
            write_to_log(f"Completed node: {func_name}")
            return result
        except Exception as e:
            write_to_log(f"Error in node {func_name}: {str(e)}")
            raise
    return wrapper
