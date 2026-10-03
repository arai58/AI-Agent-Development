from openai import OpenAI
from dotenv import load_dotenv
from embedder import load_documents,embed_contents,create_embedding
from retriever import get_best_matches
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

documents=load_documents()
document_embeddings=embed_contents(client,os.getenv("EMBEDDING_MODEL"),documents)

messages=[]
messages.append({"role":"system",
                       "content":"Answer only from provided context and nothing else."})
#print(f"number of documents found : {documents}")
#print (f"embedded documents size : {len(document_embeddings)}")

def main():
    load_dotenv()

    print("="*40)
    print("      MY AI ASSISTANT ")
    print("="*40)

    while True :
        user_input = input('\nYou : ')
        #print(user_input.lower(), " : this is user input")
        if user_input.lower() == 'quit' :
            print('Happy chating. GOODBYE !')
            break

        user_embedding=create_embedding(client,os.getenv("EMBEDDING_MODEL"),user_input)

        retrieved_items=get_best_matches(user_embedding,document_embeddings,2)
        #print (f"retirved details are {retrieved_items}")
        content=""
        for key in retrieved_items:
            content=content+documents[key]
        
        prompt=f"""Answer question only from provided information.
                    Question : {user_input}
                    context: {content}"""

        print(prompt)

        messages.append(
                {
                "role": "user",
                "content": prompt
            })

        #print(f"Prompt : {prompt}")

        #print("="*10,"going to ai","="*10)
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages)

        ai_response=response.choices[0].message.content
        print("\nAI : ", ai_response)
        messages.append({"role":"assistant","content":ai_response})

main()