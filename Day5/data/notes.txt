from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_manager import execute_tool


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
        #response=client.chat.completions.create(
         #   model=os.getenv("MODEL"),
         #   messages=messages
        #)

        #ai_response=response.choices[0].message.content
        response=execute_tool(user_message)
        if(response.lower()=="ai_run"):
            response=get_ai_response()
        
        print("\nAI : ",response)

        messages.append(buildMessage("assistant",response))





def buildMessage(role,content):

    message={
        "role":role,
        "content":content
    }
    
    return message




def get_ai_response():
    response=client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )

    return response.choices[0].message.content

main()