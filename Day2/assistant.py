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
        
        user_message={
            "role": "user"
        }



def buildMessage():

    messageObject = {
        "role": role,
        "message": message
    }

    return messageObject