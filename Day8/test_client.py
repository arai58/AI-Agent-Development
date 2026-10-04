import asyncio
from mcp_client import *

async def main():

    client=await connect()

    tools=await discover_tools(client)
    
    print("-----------------------")
    print("Available tools")
    print("-----------------------")

    for tool in tools:
        print(tool)

    result=await execute_tool(client, "roll_dice")

    print("Dice result : ", result.connect[0].text)

    await disconnect(client)

asyncio.run(main())