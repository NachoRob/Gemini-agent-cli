import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    # 1. Obtener el path absoluto del working_directory
    try:
        working_dir_abs = os.path.abspath(working_directory)

        # 2. Construir el path completo y normalizarlo para evitar "shenanigans" (.. , //)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # 3. Validar si el target_dir está dentro del working_dir_abs usando commonpath
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        # A partir de aquí el acceso es seguro

        items_info = []
        for item_name in os.listdir(target_dir):
            # Construimos la ruta completa del item para obtener sus propiedades
            item_path = os.path.join(target_dir, item_name)
            
            # Obtenemos tamaño y si es directorio
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            
            # Formateamos el string según tu requerimiento
            items_info.append(f"- {item_name}: file_size={file_size} bytes, is_dir={is_dir}")

        # Unimos todos los elementos con saltos de línea
        return "\n".join(items_info)
    except Exception as e:
        return f"Error: {str(e)}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)