"""
{{ cookiecutter.project_description }}

Bindu Agent Entry Point
"""

import argparse
import asyncio
import json
import os
from pathlib import Path
from textwrap import dedent
from typing import Any

{% if cookiecutter.agent_framework == "agno" %}
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MultiMCPTools
{% elif cookiecutter.agent_framework == "fastagent" %}
import asyncio
from fast_agent.core.fastagent import FastAgent
{% endif %}

from bindu.penguin.bindufy import bindufy


# Global MCP tools instances
mcp_tools = None  # MultiMCPTools instance
agent = None
model_name = None
_initialized = False
_init_lock = asyncio.Lock()


async def initialize_mcp_tools(env: dict = None):
    """Initialize and connect to MCP servers.

    Args:
        env: Environment variables dict for MCP servers (e.g., API keys)
    """
    global mcp_tools

    # Initialize MultiMCPTools with all MCP server commands
    # TODO: Add your MCP server commands here
    mcp_tools = MultiMCPTools(
        commands=[
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-google-maps",
        ],
        env=env or os.environ,  # Use provided env or fall back to os.environ
        allow_partial_failure=True,  # Don't fail if one server is unavailable
        timeout_seconds=30,
    )

    # Connect to all MCP servers
    await mcp_tools.connect()
    print("✅ Connected to MCP servers")


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Get path to agent_config.json in project root
    config_path = Path(__file__).parent / "agent_config.json"

    with open(config_path, "r") as f:
        return json.load(f)

{% if cookiecutter.agent_framework == "agno" %}
# Create the agent instance
async def initialize_agent():
    """Initialize the agent once."""
    global agent, model_name, mcp_tools

    agent = Agent(
        name=f"{{cookiecutter.project_name}} Bindu Agent",
        model=OpenRouter(id=model_name),
        tools=[mcp_tools],  # MultiMCPTools instance
        instructions=dedent("""\
            You are a helpful AI assistant with access to multiple capabilities including:
            - Airbnb search for accommodations and listings
            - Google Maps for location information and directions

            Your capabilities:
            - Search for Airbnb listings based on location, dates, and guest requirements
            - Provide detailed information about available properties
            - Access Google Maps data for location information and directions
            - Help users find the best accommodations for their needs

            Always:
            - Be clear and concise in your responses
            - Provide relevant details about listings and locations
            - Ask for clarification if needed
            - Format responses in a user-friendly way
        """),
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Agent initialized")


async def cleanup_mcp_tools():
    """Close all MCP server connections."""
    global mcp_tools

    if mcp_tools:
        try:
            await mcp_tools.close()
            print("🔌 Disconnected from MCP servers")
        except Exception as e:
            print(f"⚠️  Error closing MCP tools: {e}")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys

    Returns:
        Agent response
    """
    global agent

    # Extract the last user message for the agent
    user_message = next(
        (msg["content"] for msg in reversed(messages) if msg["role"] == "user"),
        ""
    )

    # Run the agent and get response
    response = await agent.arun(user_message)
    return response

{% endif %}


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys
                  e.g., [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]

    Returns:
        Agent response (ManifestWorker will handle extraction)
    """
    {% if cookiecutter.agent_framework == "agno" %}
    # Run agent with messages
    global _initialized

    # Lazy initialization on first call (in bindufy's event loop)
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing MCP tools and agent...")
            # Build environment with API keys
            env = {
                **os.environ,
                #"GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY", ""),
            }
            await initialize_all(env)
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result
    {% endif %}


async def initialize_all(env: dict = None):
    """Initialize MCP tools and agent.

    Args:
        env: Environment variables dict for MCP servers
    """
    await initialize_mcp_tools(env)
    await initialize_agent()


# Bindufy and start the agent server
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Bindu Agent with MCP Tools")
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o-mini"),
        help="Model ID to use (default: openai/gpt-4o-mini, env: MODEL_NAME)",
    )

    # If we need to pass more variables to the agent (e.g., API keys, config)
    # parser.add_argument(
    #     "--google-maps-api-key",
    #     type=str,
    #     default=os.getenv("GOOGLE_MAPS_API_KEY", ""),
    #     help="Google Maps API key (env: GOOGLE_MAPS_API_KEY)",
    # )
    args = parser.parse_args()

    # Set global model name
    model_name = args.model
    print(f"🤖 Using model: {model_name}")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        # Note: MCP tools and agent will be initialized lazily on first request
        print("🚀 Starting Bindu agent server...")
        bindufy(config, handler)
    finally:
        # Cleanup on exit
        print("\n🧹 Cleaning up...")
        asyncio.run(cleanup_mcp_tools())
