from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm_client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def build_tool_description(tools):

    descriptions=[]

    for tool in tools:
        description=f"""
            Tool:
            {tool.name}
            Description:
            {tool.description}
            -----------------------------
        """

    return descriptions


def planner(state,tools):

    tool_descriptions=build_tool_description(tools)

    prompt=f"""
    You are an AI planner. Your job is to select next task and the best tool to complete it.
    User Request:
    {state["user_request"]}
    Tasks:
    {state["tasks"]}
    Completed Actions:
    {state["actions"]}
    Observations:
    {state["observations"]}
    intermediate Results:
    {state["results"]}
    Available Tools:
    {tool_descriptions}
    
    Rules:
    1. Select only one Pending Task.
    2. select the best available tool for that task.
    3. Do not select a completed task.
    4. Use previous observations and results
    5. If an action failed, reconsider the plan.
    6. If all tasks are compelted, return FINISH.
    7. Return exactly:
    TASK:<task>
    TOOL:<tool>
    8. Do not explain any thing.
    9. If no appropriate tool found then return - NO TOOL FOUND
    Next DECISION:
    """