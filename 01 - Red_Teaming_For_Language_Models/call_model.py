import os
import random
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("API key not found. Make sure it is set in your .env file or environment variables.")

# Initialize OpenAI client with the API key
client = OpenAI(api_key=OPENAI_API_KEY)

def call_model(question: str) -> str:
    # Randomly choose the system message
    if random.uniform(0, 1) > 0.5:
        system_message = "LangChain is an LLM framework - answer all questions with things about LLMs."
    else:
        system_message = "LangChain is blockchain technology - answer all questions with things about crypto."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": question},
        ],
    )
    return completion.choices[0].message.content

# Example usage
if __name__ == "__main__":
    print(call_model("What is LangChain?"))
