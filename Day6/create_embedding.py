from openai import OpenAI
from dotenv import load_dotenv
import os
from Day6.retriever import cosine_similarity

load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


def main():

    #texts=["Python is a programming language.","Python is used for software development."]
    texts=["Python is a programming language.","Pizza is dlicious"]
    embedded_text=[]
    for text in texts:
        response=client.embeddings.create(
            model=os.getenv("EMBEDDING_MODEL"),
            input=text
        )
        temp_text=response.data[0].embedding
        embedded_text.append(temp_text)

        print("="*20,f"details of {text}","="*20)
        print(f"{type(temp_text)} : {len(temp_text)}")
        #print(len(temp_text))
        #print(response)
        #print("="*20)

    similarity=cosine_similarity(embedded_text[0],embedded_text[1])
    print(similarity)

main()
