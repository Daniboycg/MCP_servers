import os
import json
import subprocess
import sys

def setup_venv():
    # Get the absolute path to the current directory
    base_path = os.path.abspath(os.path.dirname(__file__))
    venv_path = os.path.join(base_path, 'venv')
    venv_created = False

    # Create virtual environment if it doesn't exist
    if not os.path.exists(venv_path):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)
        print("Virtual environment created successfully!")
        venv_created = True
    else:
        print("Virtual environment already exists.")
    
    # Install requirements if we just created the venv
    if venv_created:
        print("\nInstalling requirements...")
        # Use the venv's pip to install requirements
        pip_path = os.path.join(venv_path, 'Scripts', 'pip.exe')
        requirements_path = os.path.join(base_path, 'requirements.txt')
        subprocess.run([pip_path, 'install', '-r', requirements_path], check=True)
        print("Requirements installed successfully!")

def generate_mcp_config():
    # Get the absolute path to the current directory
    base_path = os.path.abspath(os.path.dirname(__file__))
    
    # Construct the paths
    python_path = os.path.join(base_path, 'venv', 'Scripts', 'python.exe')
    server_script_path = os.path.join(base_path, 'mcp_server.py')
    
    # Create the config dictionary
    config = {
        "mcpServers": {
            "archon": {
                "command": python_path,
                "args": [server_script_path]
            }
        }
    }
    
    # Write the config to a file
    config_path = os.path.join(base_path, 'mcp-config.json')
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"\nMCP configuration has been written to: {config_path}")    
    print(f"\nMCP configuration for Cursor:\n\n{python_path} {server_script_path}")
    print("\nMCP configuration for Windsurf/Claude Desktop:")
    print(json.dumps(config, indent=2))

if __name__ == '__main__':
    setup_venv()
    generate_mcp_config()
