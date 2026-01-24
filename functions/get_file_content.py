import os
from config import MAX_CHARS
from google import genai
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        abs_file_path = os.path.abspath(full_path)
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else: 
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read(MAX_CHARS)
                if f.read(1):
                    content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return content
            
    except Exception as e:
       return str(e)
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["working_directory", "file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)"
            ),
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory from which file paths are resolved"
            ),
        },
    ),
)