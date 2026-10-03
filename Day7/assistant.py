from openai import OpenAI
from dotenv import load_dotenv
import os
#from tool_manager import execute_tool
from planner import choose_tool
import tools

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
        #print(f"selected tool is {tool_name}")

        messages.append(build_message("user",user_message))
        
        result=""
        if(tool_name != "none"):
            if hasattr(tools, tool_name):
                func_to_call = getattr(tools, tool_name)
                result = func_to_call()
                #print(result)
            else:
                print(f"Function '{tool_name}' not found in the module.")
        else:
            result="no appropriate tool found"
        #if(response.lower()=="none"):
        #    response=get_ai_response()
        prompt=f"""user as asked for {user_message} and tool has returned {result}.
        response to user naturally.dont not add other information from your side."""

        messages.append(build_message("user",prompt))

        ai_response=get_ai_response()
        #ai_response=response.choices[0].message.content
        print("\nAI : ", ai_response)

        messages.append(build_message("assistant",ai_response))





def build_message(role,content):

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