import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 3. Validar si el target_file_path está dentro del working_dir_abs usando commonpath
        valid_target_file = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        else:
            command = ["python", target_file_path]
            if args:
                command.extend(args)
            result = subprocess.run(
                    command, 
                    capture_output=True, 
                    text=True, 
                    cwd=working_dir_abs, 
                    timeout=30
            )
            if result.returncode != 0:
                return f"Process exited with code {result.returncode}"
            if not result.stdout.strip() and not result.stderr.strip():
                return "No output produced"
            output_parts = []
            if result.stdout.strip():
                output_parts.append(f"STDOUT: {result.stdout.strip()}")
            if result.stderr.strip():
                output_parts.append(f"STDERR: {result.stderr.strip()}")
            return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"    