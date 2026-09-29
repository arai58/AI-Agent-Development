from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

roles={
    "1": "You are an english teacher. Who is kind and always encouraging. Identify and explain mistkaes in simple and polite terms",
    "2": "You are German teacher, who is helping prepare students prepare for their exams. You are polite, supportive and encourgaing",
    "3": "You are communication and speech trainer. You find and suggest a Professional way to write and speak for level of MD. You explain what, why and how it is better than original version.",
    "4": "You are a mind refresher, casual chatty friend who helps loosen enviornment and relax their best friend."
}

rolesChoices={
    "1":"English Teacher",
    "2":"German Teacher - preparing for exam",
    "3":"Communication and Speech Trainer",
    "4":"Friend"
}

messages=[]

def main():

    print("="*40)
    print("  MY AI ASSISTANT")
    print("="*40)

    print("Hey, welcome to your AI Assitant. Let me know how you want me to support you :")
    for key, value in rolesChoices.items() :
        print(f"{key} : {value}")

    choice=input("Enter your choice : ")

    messages.append(buildMessage("system",rolesChoices[choice]))

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
        messages.append(buildMessage("AI",ai_reply))

        print("\nAI : ", ai_reply)



def buildMessage(role, message):

    messageObject = {
        "role": role,
        "content": message
    }

    return messageObject


main()