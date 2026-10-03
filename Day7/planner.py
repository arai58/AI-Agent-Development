from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


def choose_tool(user_request):
    planner_prompt=f"""
    you are an AI planner. 
    Available tools:
    1. get_current_time
        use when the user asks for current date or time and enquire about date and time.
    2. roll_dice
        use when the user asks to roll a dice or when want to place any dice based game.
    3. generate_password
        use when the user asks to geenrate sucure passcode or password.
    if no tool found then return none.
    Always return tool name only. no description of any other information.
    content: {user_request}"""

    messages=[
        {"role":"system",
        "content":"You are any AI Planner"},
        {"role":"user",
        "content":planner_prompt}
    ]

    response=client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    return response.choices[0].message.content.strip()