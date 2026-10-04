from fastmcp import Client


async def connect():
    """
    Connect to the MCP Server.
    """
    client=Client("server.py")
    await client.__aenter__()
    print("Conected to MCP server")
    return client


async def disconnect(client):
    """
    Disconnect from MCP server.
    """
    await client.__aexit__(
        None,
        None,
        None
    )
    print("Disconnected from server.")


async def discover_tools(client):
    """
    Returns available tools list in MCP server.
    """
    tools=await client.list_tools()
    return tools

async def execute_tool(client,tool_name,arguments=None):
    """
    Execute tool and return output to AI agent.
    """
    if arguments==None:
        arguments={}
    
    result=await client.call_tool(tool_name,arguments)

    return result
