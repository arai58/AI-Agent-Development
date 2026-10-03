from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


def main():

    texts=["Python is a programming language.","Python is used for software development."]
    embedded_text=[]
    for text in texts:
        response=client.embedding.create(
            model=os.getenv("EMBEDDING_MODEL"),
            input=text
        )
    temp_text=response.data[0].embedding
    embedded_text.append(temp_text)

    print("="*20,f"details of {text}","="*20)
    print(type(temp_text))
    print(len(temp_text))
    print(response)
    print("="*20)

main()
