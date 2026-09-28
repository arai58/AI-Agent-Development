from openai import OpenAI;
from dotenv import load_dotenv;
import os;


load_dotenv()

print(os.getenv("BASE_URL"), " : ", os.getenv("API_KEY"))

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
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages= messages
    )
    print("Messages response")
    print(response.choices[0].message.content)


main()