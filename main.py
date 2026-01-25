import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from functions.call_function import call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found, please add it to your .env file")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="La pregunta o prompt para el modelo")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    available_functions = types.Tool(
        function_declarations=[schema_get_files_info,
                               schema_get_file_content,
                               schema_run_python_file,
                               schema_write_file],
    )

    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt))

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if not response.function_calls:
            print(response.text)
            break
        
        if response.function_calls:
            function_results = []
            
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)
                #2. Validación: ¿Tiene partes?
                if not function_call_result.parts:
                    raise Exception("The function call result has no parts.") 
                if function_call_result.parts[0].function_response is None:
                    raise Exception("The first part is not a FunctionResponse.")
                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("The function response field is empty.")
                
                # Aquí es donde cambias la lógica de impresión
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                else:
                    # Si no está en modo verbose, imprime el resultado directamente
                    # Esto es crucial para que el test de lorem.txt lo encuentre
                    resultado_final = function_call_result.parts[0].function_response.response["result"]
                    print(resultado_final)
                
                # 3. Guardas la parte
                function_results.append(function_call_result.parts[0])
            messages.append(types.Content(role="user", parts=function_results))    

        else:
            print(response.text)
    else:
        print(f"Error: Maximum iterations (20) reached without a final response.")
        exit(1)

if __name__ == "__main__":
    main()