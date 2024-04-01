import os
from src.const_parameters import *

def change_extension(filename, ext):
    base_name, extension = os.path.splitext(filename)
    return f"{base_name}{ext}"

def get_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files