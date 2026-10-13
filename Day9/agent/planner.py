from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def planner(state, tools_list):

    tool_descriptions=build_tool_description(tools_list)

    prompt=f"""
    You are an AI Planner. Your job is to identify, select and return next action only.
    User Request : {state["user_request"]}
    Tools Description/List : {tool_descriptions}
    Completed Actions : {state["actions"]}
    Previous Observations: {state["observations"]}
    Instructions:
    1. You have select best tool suitable for idenfited action.
    2. Next action/tool should be only from supplied list
    3. Return only one action at a time
    4. Never repeat action that has been already completed.
    5. Use the observations to decide what is still required.
    6. Return only tool name or FINISH
    7. No Suitable tool is found for identifed action and it is last then return ERROR.
    8. Return only action/tool name. Don't provide any explain or additional detail.
    """

    response=client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"system",
                "content":"You are AI system and helps in planning next actions"
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    if response.choices[0] :
        tool_name=response.choices[0].message.content
    else:
        tool_name="ERROR"

    return tool_name.strip()


def build_tool_description(tools_list):
    description=""
    for tool in tools_list:
        description+=f"""
        Name: {tool.name}
        Description: {tool.description}
        -------------------------------------
        """
    
    return description