import os
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    # 1. Obtener el path absoluto del working_directory
    try:
        working_dir_abs = os.path.abspath(working_directory)

        # 2. Construir el path completo y normalizarlo para evitar "shenanigans" (.. , //)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 3. Validar si el target_file_path está dentro del working_dir_abs usando commonpath
        valid_target_file = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        # A partir de aquí el acceso es seguro
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file.",
            ),
         },
         required=["file_path", "content"],
    ),
)
