import os
from datetime import datetime
from functools import wraps
import inspect

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
