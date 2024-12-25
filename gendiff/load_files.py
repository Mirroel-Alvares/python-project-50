import os
import json
import sys


def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File is not a valid JSON - {file_path}")
        sys.exit(1)


def load_files(filename, search_path=None):
    if search_path is None:
        search_path = os.path.dirname(os.path.abspath(__file__))

    if os.path.isabs(filename):
        return load_json(filename)

    file_path = find_file(filename, search_path)
    if file_path is not None:
        return load_json(file_path)

    return None
