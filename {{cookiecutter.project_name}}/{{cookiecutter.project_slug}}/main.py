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
{% elif cookiecutter.agent_framework == "crewai" %}
from crewai import Agent
from crewai.tools import tool
from langchain_openai import ChatOpenAI
{% elif cookiecutter.agent_framework == "langchain" %}
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
{% endif %}

from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Global MCP tools instances
mcp_tools: Any | None = None
agent: Any | None = None
model_name: str | None = None
openrouter_api_key: str | None = None
mem0_api_key: str | None = None
_initialized = False
_init_lock = asyncio.Lock()


async def initialize_mcp_tools(env: dict[str, str] | None = None) -> None:
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
        env=env or dict(os.environ),  # Use provided env or fall back to os.environ
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
        ] if tool is not None],  # MultiMCPTools instance
        instructions=[dedent("""\
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
    """Run the agent with the given messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys

    Returns:
        Agent response
    """
    global agent

    # Run the agent and get response
    response = await agent.arun(messages)
    return response

{% elif cookiecutter.agent_framework == "crewai" %}
# Create the agent instance
async def initialize_agent() -> None:
    """Initialize the CrewAI agent once."""
    global agent, model_name, mcp_tools

    if not model_name:
        msg = "model_name must be set before initializing agent"
        raise ValueError(msg)

    llm = ChatOpenAI(
        model=model_name,
        api_key=openrouter_api_key,
        temperature=0.7
    )

    agent = Agent(
        role=f"{{cookiecutter.project_name}} Assistant",
        goal=dedent("""\
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
        backstory="You are an AI assistant specialized in helping users find accommodations and location information.",
        llm=llm,
        tools=[tool for tool in [
            mcp_tools,
            Mem0Tools(api_key=mem0_api_key)
        ] if tool is not None] if mcp_tools or mem0_api_key else [],
        verbose=True,
        allow_delegation=False,
    )
    print("✅ CrewAI Agent initialized")


async def cleanup_mcp_tools() -> None:

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

    # Run the agent and get response
    response = await agent.arun(messages)
    return response

{% elif cookiecutter.agent_framework == "langchain" %}
# Create the agent instance
async def initialize_agent() -> None:
    """Initialize the LangChain agent once."""
    global agent, model_name, mcp_tools, agent_executor

    if not model_name:
        msg = "model_name must be set before initializing agent"
        raise ValueError(msg)

    llm = ChatOpenAI(
        model=model_name,
        api_key=openrouter_api_key,
        temperature=0.7
    )

    # Create tools list
    tools = []
    if mcp_tools:
        tools.extend(mcp_tools.get_tools())
    
    # Add Mem0Tools if API key is available
    if mem0_api_key:
        tools.append(Mem0Tools(api_key=mem0_api_key))
    
    # Create the agent with instructions
    from langchain import hub
    prompt = hub.pull("hwchase17/openai-tools-agent")
    
    # Create a custom prompt with instructions
    from langchain_core.prompts import ChatPromptTemplate
    system_prompt = dedent("""\
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
    """)
    
    agent_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
        ("assistant", "{agent_scratchpad}")
    ])
    
    agent = create_tool_calling_agent(llm, tools, agent_prompt)
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,
        return_intermediate_steps=True
    )
    
    print("✅ LangChain Agent initialized")


async def cleanup_mcp_tools() -> None:
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
    
    # Run the agent and get response
    response = await agent.arun(messages)
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
    {% if cookiecutter.agent_framework in ["agno", "crewai", "langchain"] %}
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


async def initialize_all(env: Optional[dict[str, str]] = None):
    """Initialize MCP tools and agent.

    Args:
        env: Environment variables dict for MCP servers
    """
    #await initialize_mcp_tools(env)
    await initialize_agent()


def main():
    """Run the Agent."""
    global model_name, api_key, mem0_api_key

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Bindu Agent with MCP Tools")
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-oss-120b:free"),
        help="Model ID to use (default: openai/gpt-oss-120b:free, env: MODEL_NAME), if you want you can use any free model: https://openrouter.ai/models?q=free",
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

    # Set global model name and API keys
    model_name = args.model
    openrouter_api_key = args.api_key
    mem0_api_key = args.mem0_api_key

    if not openrouter_api_key:
        raise ValueError("OPENROUTER_API_KEY required") # noqa: TRY003
    if not mem0_api_key:
        raise ValueError("MEM0_API_KEY required. Get your API key from: https://app.mem0.ai/dashboard/api-keys") # noqa: TRY003

    print(f"🤖 Using model: {model_name}")
    print("🧠 Mem0 memory enabled")

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


# Bindufy and start the agent server
if __name__ == "__main__":
    main()
