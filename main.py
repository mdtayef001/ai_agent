import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("api_key invalid")

    client = genai.Client(api_key=api_key)
    message = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_content(client, message)


def generate_content(client, message):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=message
    )

    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata invalid - API request likely failed")

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(f"User prompt: {message[0].parts[0].text}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
