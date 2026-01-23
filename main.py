import argparse
import os

from dotenv import load_dotenv
from google import genai


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("api_key invalid")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=args.user_prompt
    )

    # Verification of metadata
    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata invalid - API request likely failed")

    # Accessing the counts
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    # Printing in the exact requested format
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
