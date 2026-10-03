from openai import OpenAI
from dotenv import load_dotenv
import os
#from tool_manager import execute_tool
from planner import choose_tool

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

        #get tool
        tool_name=choose_tool(user_message)
        print("selected tool is {tool}")

        messages.append(buildMessage("user",user_message))
        
        result=""
        if(tool_name != "none"):
            if hasattr(my_other_file, func_var):
                func_to_call = getattr(my_other_file, func_var)
                result = func_to_call()
                #print(result)
            else:
                print(f"Function '{func_var}' not found in the module.")
        else:
            result="no appropriate tool found"
        #if(response.lower()=="none"):
        #    response=get_ai_response()
        
        print("\nAI : ", result)

        messages.append(buildMessage("assistant",result))





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