# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""{{cookiecutter.project_name}} - An Bindu Agent.

"""

import argparse
import asyncio
import json
import os
from pathlib import Path
from textwrap import dedent
from typing import Any, Optional

{% if cookiecutter.agent_framework == "agno" %}
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MultiMCPTools
from agno.tools.mem0 import Mem0Tools
from agno.team import Team
{% elif cookiecutter.agent_framework == "fastagent" %}
import asyncio
from fast_agent.core.fastagent import FastAgent
{% elif cookiecutter.agent_framework == "autogen" %}
import autogen
{% endif %}

from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Global variables
model_name: str | None = None
openrouter_api_key: str | None = None
mem0_api_key: str | None = None

{% if cookiecutter.agent_framework == "agno" %}
# Global MCP tools instances
mcp_tools: MultiMCPTools | None = None
agent: Agent | Team | None = None
_initialized = False
_init_lock = asyncio.Lock()


async def initialize_mcp_tools(env: dict[str, str] | None = None) -> None:
    """Initialize and connect to MCP servers."""
    global mcp_tools

    mcp_tools = MultiMCPTools(
        commands=[
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-google-maps",
        ],
        env=env or dict(os.environ),
        allow_partial_failure=True,
        timeout_seconds=30,
    )

    await mcp_tools.connect()
    print("✅ Connected to MCP servers")


async def initialize_agent() -> None:
    """Initialize the agent once."""
    global agent, model_name, mcp_tools

    if not model_name:
        msg = "model_name must be set before initializing agent"
        raise ValueError(msg)

    agent = Agent(
        name=f"{{cookiecutter.project_name}} Bindu Agent",
        model=OpenRouter(
            id=model_name,
            api_key=openrouter_api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        tools=[tool for tool in [
            mcp_tools,
            Mem0Tools(api_key=mem0_api_key)
        ] if tool is not None],
        instructions=[dedent("""\
            You are a helpful AI assistant.
        """)],
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Agent initialized")


async def cleanup_mcp_tools()-> None:
    """Close all MCP server connections."""
    global mcp_tools

    if mcp_tools:
        try:
            await mcp_tools.close()
            print("🔌 Disconnected from MCP servers")
        except Exception as e:
            print(f"⚠️  Error closing MCP tools: {e}")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages."""
    global agent
    response = await agent.arun(messages)
    return response


async def initialize_all(env: Optional[dict[str, str]] = None):
    """Initialize MCP tools and agent."""
    await initialize_agent()
{% endif %}


def load_config() -> dict:
    """Load agent configuration from project root."""
    config_path = Path(__file__).parent / "agent_config.json"
    with open(config_path, "r") as f:
        return json.load(f)


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages."""
    
    {% if cookiecutter.agent_framework == "agno" %}
    # Run agent with messages
    global _initialized

    # Lazy initialization on first call
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing MCP tools and agent...")
            env = {**os.environ}
            await initialize_all(env)
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result

    {% elif cookiecutter.agent_framework == "autogen" %}
    global model_name, openrouter_api_key
    
    # 1. Setup the Autogen Config
    config_list = [{
        "model": model_name,
        "api_key": openrouter_api_key,
        "base_url": "https://openrouter.ai/api/v1"
    }]

    # 2. Create the Assistant
    assistant = autogen.AssistantAgent(
        name="Bindu_Assistant",
        llm_config={"config_list": config_list},
        system_message="You are a helpful AI assistant connected to the Bindu network."
    )

    # 3. Create a User Proxy
    user_proxy = autogen.UserProxyAgent(
        name="User_Proxy",
        human_input_mode="NEVER",
        code_execution_config=False,
    )

    # 4. Generate a reply
    last_user_message = messages[-1]["content"] if messages else "Hello"
    chat_res = await user_proxy.a_initiate_chat(
        assistant,
        message=last_user_message,
        summary_method="last_msg"
    )
    
    return chat_res.summary
    {% endif %}


def main():
    """Run the Agent."""
    global model_name, api_key, mem0_api_key

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Bindu Agent")
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-oss-120b:free"),
        help="Model ID to use.",
    )

    parser.add_argument(
        "--api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--mem0-api-key",
        type=str,
        default=os.getenv("MEM0_API_KEY"),
        help="Mem0 API key (env: MEM0_API_KEY)",
    )
    args = parser.parse_args()

    model_name = args.model
    openrouter_api_key = args.api_key
    mem0_api_key = args.mem0_api_key

    if not openrouter_api_key:
        raise ValueError("OPENROUTER_API_KEY required") # noqa: TRY003
    if not mem0_api_key:
        raise ValueError("MEM0_API_KEY required.") # noqa: TRY003

    print(f"🤖 Using model: {model_name}")
    
    config = load_config()

    try:
        print("🚀 Starting Bindu agent server...")
        bindufy(config, handler)
    finally:
        print("\n🧹 Cleaning up...")
        {% if cookiecutter.agent_framework == "agno" %}
        asyncio.run(cleanup_mcp_tools())
        {% endif %}

if __name__ == "__main__":
    main()