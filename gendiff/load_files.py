import json
import os


def load_files(filename, search_path=None):
    if search_path is None:
        search_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for root, dirs, files in os.walk(search_path):
        if filename in files:
            file_path = os.path.join(root, filename)
            try:
                 with open(file_path, 'r') as file:
                     return json.load(file)
            except FileNotFoundError:
                 print(f"Error: File not found - {file_path}")
                 sys.exit(1)
            except json.JSONDecodeError:
                 print(f"Error: File is not a valid JSON - {file_path}")
                 sys.exit(1)
    return None
