from openai import OpenAI
from dotenv import load_dotenv
from mcp_client import *
import os, asyncio


load_dotenv()

#LLM connection
llm_client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


async def main():
    mcp_client=await connect()

    tools_list=await discover_tools(mcp_client)
    
    for tool in tools_list:
        print(f"{tool.name} : {tool.description}")

    ##Gte user input
    user_request=input("User : ")


    #Select appropriate tool using LLM
    tool_name=planner(user_request,tools_list)
    #print(f"LLM has selcted tool for work : {tool_name}")

    #Exeute Tool and get response
    mcp_response=await execute_tool(mcp_client, tool_name)
    #print(f"tool response is : {mcp_response}")
    #Disconnect MCP
    await disconnect(mcp_client)

    #format response in Natural Language
    final_response=generate_response(user_request,mcp_response)

    print(f"AI : {final_response}")


def build_tool_description(tools_list):

    descriptions=""
    
    for tool in tools_list:
        #print(tool)
        descriptions+=f"""
        Tool:
        {tool.name}
        Description:
        {tool.description}
        ------------------------------
        """
    
    return descriptions

def planner(user_request,tools_list):

    tool_description=build_tool_description(tools_list)
    #print(tool_description)
    prompt=f"""
    You are an AI Planner. 
    Tools list/details:
    {tool_description}
    User Request:
    {user_request}
    Instructions:
    1. Select best tool to support user request
    2. Only tool name and no other detail or description
    3. Select tool only from provided tool list.
    4. If no correct tool is found then return none.
    """

    response=llm_client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[{"role":"user",
        "content":prompt
        }]
    )

    tool_name=response.choices[0].message.content

    return tool_name.strip()

def generate_response(user_request,tool_response):

    prompt=f"""
        The user asked : {user_request}
        mcp returned : {tool_response}
        answer in natural language. Don't add any other information out side of tool response.
        your job is to make it sound natual.
    """

    response=llm_client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]       
    )

    return response.choices[0].message.content

if __name__=="__main__":
    asyncio.run(main())