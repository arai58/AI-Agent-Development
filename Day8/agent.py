from openai import OpenAI
from dotenv import load_dotenv
from mcp_client import *
import os


load_dotenv()

#LLM connection
llm_client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


async def main():
    mcp_client=await connect()

    tools_list=await discover_tools(mcp_client)

    for tool_name,descritpion in tools_list.items():
        print(f"{tool_name} : {descritpion}")


def build_tool_description(tools_list):

    descriptions=""

    for tool_name,description in tools_list.items():
        descriptions+=f"""
        Tool:
        {tool_name}
        Description:
        {description}
        ------------------------------
        """
        return descriptions