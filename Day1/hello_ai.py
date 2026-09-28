from openai import OpenAI;
from dotenv import load_dotenv;
import os;

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages = [
    {
        "role": "user",
        "content": "What is artifical Intelligence?"
    }
]

def main():
    load_dotenv()
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages= messages
    )
