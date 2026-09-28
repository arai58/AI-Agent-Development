from openai import OpenAi
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAi(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages=[]

def main():

    print("="*40)
    print("  MY AI ASSISTANT")
    print("="*40)

    while(True):

        user_input=input("\nUser : ")

        if user_input.lower() == "quit":
            print("Goodbye !")
            break
        
        messages.append(buildMessage("user",user_input))

        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )
        
        ai_reply=response.choices[0].message.content
        messages.append("AI",ai_reply)

        print("\nAI : ", ai_reply)



def buildMessage(role, message):

    messageObject = {
        "role": role,
        "content": message
    }

    return messageObject