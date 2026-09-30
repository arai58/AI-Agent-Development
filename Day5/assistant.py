from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_manager import execute_tool
from tools import read_file


load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages=[]

file_content=""

def main():

    print("="*40)
    print("     MY AI ASSITANT")
    print("="*40)

    while(True):
        user_message=input("\nUSER : ")
        
        if(user_message.lower()=="quit"):
            print("\nGOODBYE!")
            break

        user_input_lower=user_message.lower()
        filename="data/"
        ask_type=""
        ask_length=0

        if(user_input_lower.startswith("summarize")):
            ask_type="Summarize"
            ask_length=20
        elif(user_input_lower.startswith("explain")):
            ask_type="Explain"
            ask_length=100        

        filename=filename+user_message[ask_type.length()+1:].strip()
        file_content=read_file(filename)
        
        if(file_content.lower=="filenotfound"):
            print("\nAI : Your file does not exists.")
        
        

        prompt=f"""{ask_type} {filename} document content in less than {ask_length} words.
                    Document:
                    {file_content}"""

        messages.append(buildMessage("user",prompt))
        #response=client.chat.completions.create(
         #   model=os.getenv("MODEL"),
         #   messages=messages
        #)

        #ai_response=response.choices[0].message.content
        #response=execute_tool(user_message)
        #if(response.lower()=="ai_run"):
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