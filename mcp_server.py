"""
kiteMCP - Main MCP Server for Options Trading
Handles authentication and orchestrates tools, prompts, and resources.
"""

from mcp.server.fastmcp import FastMCP
from kiteconnect import KiteConnect
from getpass import getpass
import os

# Initialize FastMCP server
mcp = FastMCP("kiteMCP")

# Global kite instance
kite = None

def authenticate_kite():
    """Handle Kite Connect authentication at server startup (not exposed as a tool)"""
    global kite
    
    # Get API credentials
    API_KEY = os.getenv("KITE_API_KEY") or input("Enter your Kite API Key: ")
    API_SECRET = os.getenv("KITE_API_SECRET") or getpass("Enter your Kite API Secret: ")
    
    # Initialize Kite Connect
    kite = KiteConnect(api_key=API_KEY)
    
    # Get login URL and handle authentication
    print("\nGo to this URL and login to your Zerodha account:")
    print(kite.login_url())
    request_token = input("\nPaste the request_token from the redirected URL here: ").strip()
    
    try:
        data = kite.generate_session(request_token, api_secret=API_SECRET)
        kite.set_access_token(data["access_token"])
        print("Kite session authenticated successfully!")
        return True
    except Exception as e:
        print(f"Authentication failed: {e}")
        return False

def register_components():
    """Register all components with the MCP server."""
    # Set the kite instance in tools module
    from tools import set_kite_instance, set_mcp_instance as set_tools_mcp, register_tools
    set_kite_instance(kite)
    set_tools_mcp(mcp)
    register_tools()
    
    # Set the MCP instance in prompts module
    from prompts import set_mcp_instance as set_prompts_mcp, register_prompts
    set_prompts_mcp(mcp)
    register_prompts()
    
    # Set the MCP instance in resources module
    from resources import set_mcp_instance as set_resources_mcp, register_resources
    set_resources_mcp(mcp)
    register_resources()

if __name__ == "__main__":
    # Authenticate at startup (before starting MCP server)
    if authenticate_kite():
        print("Starting kiteMCP server with modular components...")
        
        # Register all components
        register_components()
        
        # Start the server
        mcp.run(transport='stdio')
    else:
        print("Failed to authenticate. Exiting.")