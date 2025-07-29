import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY") or "xai-6zsoonNPiOQvqcvtewZHOzjMc9tp58iYIibHvgznqNaiDqU8cKM0JXJUsOg1n7d5lBwhIwqVGhHLwN8Z"
GROK_API_URL = "https://api.x.ai/v1/chat/completions"


def call_grok_api(messages, model="grok-3-latest", temperature=0):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROK_API_KEY}"
    }
    payload = {
        "messages": messages,
        "model": model,
        "stream": False,
        "temperature": temperature
    }

    response = requests.post(GROK_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Something went wrong while calling the Grok API."


def main():
    print("Welcome! I'm your Grok-powered assistant. Type 'quit' to exit.")
    
    # Optional: Define a system prompt for consistent behavior
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant. Keep your answers short and clear."
    }

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            break

        messages = [
            system_message,
            {"role": "user", "content": user_input}
        ]

        reply = call_grok_api(messages)
        print(f"\nAssistant: {reply}")


if __name__ == "__main__":
    main()
