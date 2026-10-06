from datetime import datetime
import string
import secrets
import random
from fastmcp import FastMCP
from mcp.server.mcpserver import MCPServer


mcp=FastMCP("My MCP Server")

@mcp.tool()
def current_time():
    """
    Returns the current date and time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")



@mcp.tool()
def roll_dice():
    """
    Returns a number after rolling dice of 6.
    """
    return random.randint(1,6)

@mcp.tool()
def generate_password(length: int = 12):
    """
    Returns a random password generated of asked length or default to legnth of 12. It uses randmly
    Lower case, uppercase, ascii_letters, digits, punctuation.
    """

    character_list=(string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits)
    
    password=""

    for _ in range(length):
        password+=secrets.choice(character_list)

    return password

if __name__=="__main__":
    print("Staring MCP Server....")
    mcp.run()