"""
{{ cookiecutter.project_description }}

Bindu Agent Entry Point
"""

import json
import os
from pathlib import Path
from typing import Any

{% if cookiecutter.agent_framework == "agno" %}
from agno.agent import Agent
from agno.models.openai import OpenAIChat
{% elif cookiecutter.agent_framework == "fastagent" %}
import asyncio
from fast_agent.core.fastagent import FastAgent
{% endif %}

from bindu.penguin.bindufy import bindufy


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Get path to agent_config.json in project root
    project_root = Path(__file__).parent.parent
    config_path = project_root / "agent_config.json"
    
    with open(config_path, "r") as f:
        return json.load(f)


# Load configuration
config = load_config()

# Check if OpenAI key is available
openai_key = os.getenv("OPENAI_API_KEY")

{% if cookiecutter.agent_framework == "agno" %}
# Create the agent instance
if openai_key:
    # REAL MODE - with OpenAI
    agent = Agent(
        instructions=config.get("description", "Provide helpful responses to user messages"),
        model=OpenAIChat(id="gpt-4o", api_key=openai_key),
    )
    print("✅ Agent running with OpenAI GPT-4")
else:
    # MOCK MODE - for development without API key
    print("⚠️  Running in MOCK mode (no OPENAI_API_KEY found)")
    print("   Add OPENAI_API_KEY to .env for real AI responses")
    agent = Agent(
        instructions=config.get("description"),
        model=None,
    )
{% elif cookiecutter.agent_framework == "langchain" %}
# Create LangChain agent
if openai_key:
    llm = ChatOpenAI(temperature=0, api_key=openai_key)
    agent = Agent(llm=llm)
    print("✅ Agent running with OpenAI")
else:
    print("⚠️  Running in MOCK mode (no OPENAI_API_KEY found)")
    agent = None
{% endif %}


def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages.
    
    Args:
        messages: List of message dicts with 'role' and 'content' keys
                  e.g., [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]
    
    Returns:
        Agent response (ManifestWorker will handle extraction)
    """
    if not openai_key:
        # Mock response in development mode
        last_message = messages[-1].get("content", "") if messages else ""
        return {"content": f"[MOCK] Echo: {last_message}"}
    
    {% if cookiecutter.agent_framework == "agno" %}
    # Run agent with messages
    result = agent.run(input=messages)
    return result


if __name__ == "__main__":
    print(f"🚀 Starting Bindu Agent: {config['name']}")
    print(f"   Version: {config['version']}")
    print(f"   Author: {config['author']}")
    print(f"   Port: {config['deployment']['url']}")
    
    # Bindufy and start the agent server
    bindufy(agent, config, handler)