from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages=[]



def main():

    print("="*40)
    print("     MY AI ASSITANT")
    print("="*40)

    while(True):
        user_message=input("\nUSER : ")
        
        if(user_message.lower()=="quit"):
            print("\nGOODBYE!")
            break


        messages.append(buildMessage("user",user_message))
        response=client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )

        ai_response=response.choices[0].message.content
        print("\nAI : ",ai_response)

        messages.append(buildMessage("assistant",ai_response))





def buildMessage(role,content):

    message={
        "role":role,
        "content":content
    }
    
    return message


main()