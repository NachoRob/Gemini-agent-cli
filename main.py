import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content

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
                               schema_get_file_content],
    )

    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt))

    if response.function_calls:
    
        # 2. Iteramos sobre la lista de llamadas
        for function_call in response.function_calls:
            # 3. Imprimimos el nombre y los argumentos como pide la instrucción
            print(f"Calling function: {function_call.name}({function_call.args})")
            
    else:
        print(response.text)


if __name__ == "__main__":
    main()
