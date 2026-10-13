from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio

from mcp_client import *

from agent.planner import planner
from agent.executor import execute_action
from agent.loop import run_agent_loop

load_dotenv()

llm_client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


def format_answer(state):
    prompt=f"""
    the user asked:
    {state["user_request"]}
    actions performed:
    {state["actions"]}
    all observations:
    {state["observations"]}

    Answer the user Naturally. No additional infomration or explanation to be provided.
    Don't mention state or internal details.
    """

    response=client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()

async def main():
    client=await connect()

    tools_list=await discover_tools(client)

    user_input=input("\nUSER : ")

    state=await run_agent_loop(user_input,planner,execute_action,
    format_answer,tools_list,client)

    print(f"""\nAI : {state["final_answer"]}""")

    await disconnect(client)

if __name__=="__main__":
    asyncio.run(main())