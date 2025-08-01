import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Groq API settings
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

# Initialize Groq client
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Required for Groq
)

# Main LLM call function
def call_llm(prompt: str, system_message="You are a helpful job application assistant."):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1024,
    )
    return response.choices[0].message.content.strip()
    