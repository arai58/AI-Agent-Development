from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

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

        
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[{
                "role": "user",
                "content": user_input
            }]
        )

        print("\nAI : ", response.choices[0].message.content)

main()