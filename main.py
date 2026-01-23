import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("api_key invalid")

    client = genai.Client(api_key=api_key)
    user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    # FIX: Changed model to 2.0-flash
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_prompt
    )

    # Verification of metadata
    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata invalid - API request likely failed")

    # Accessing the counts
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    # Printing in the exact requested format
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
