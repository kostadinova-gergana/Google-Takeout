import os
import subprocess

# Define the paths to the four scripts
script_paths = [
    "path/to/zip.py",
    "path/to/merge.py",
    "path/to/metadata.py",
    "path/to/bymonth.py"
]

def execute_scripts(script_paths):
    for script_path in script_paths:
        print(f"Executing script: {script_path}")
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Script execution successful: {script_path}")
        else:
            print(f"Error executing script: {script_path}")
            print(f"Output: {result.stdout}")
            print(f"Error: {result.stderr}")

def main():
    execute_scripts(script_paths)

if __name__ == "__main__":
    main()
