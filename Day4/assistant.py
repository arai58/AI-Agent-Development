from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import(get_current_time,roll_dice,generate_password)


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
        reponse=get_response(user_message)
        print("\nAI : ",response)

        messages.append(buildMessage("assistant",response))





def buildMessage(role,content):

    message={
        "role":role,
        "content":content
    }
    
    return message


def get_response(user_intent):

    user_intent_lower = user_intent.lower()
    output=""
    if "time" in user_intent_lower or "clock" in user_intent_lower:
        output="current time is " + get_current_time()
    elif "password" in user_intent_lower or "passcode" in user_intent_lower:
        output="Your generated password of length 12 is " + generate_password(12)
    elif "dice" in user_intent_lower or "die" in user_intent_lower:
        output="You rolled "+roll_dice()
    else:
        output=get_ai_response()

    return output

def get_ai_response():
    response=client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )

    return response.choices[0].message.content

main()