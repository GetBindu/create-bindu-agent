<p align="center">
  <img src="assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> Create Bindu Agent 🌻</h1>

<p align="center">
  <em>"We imagine a world of agents where they can communicate with each other seamlessly.<br/>
  And Bindu turns your agent into a living server , the dot (Bindu) in the Internet of Agents."</em>
</p>

<br/>

[![GitHub License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Hits](https://hits.sh/github.com/Saptha-me/create-bindu-agent.svg)](https://hits.sh/github.com/Saptha-me/create-bindu-agent/)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Saptha-me/create-bindu-agent/pulls)
[![Join Discord](https://img.shields.io/badge/Join%20Discord-7289DA?logo=discord&logoColor=white)](https://discord.gg/3w5zuYUuwt)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.saptha.me)
[![GitHub stars](https://img.shields.io/github/stars/Saptha-me/create-bindu-agent)](https://github.com/Saptha-me/create-bindu-agent/stargazers)

<br/>


## From Zero to Production-Ready Agent in 2 Minutes

**Create Bindu Agent** is the fastest way to build production-ready AI agents that speak the language of the Internet of Agents. No boilerplate. No configuration hell. Just configure and get a fully deployable agent that communicates using **A2A**, **AP2**, and **X402** protocols.

<br/>

## Quickstart

**Time to first agent: ~2 minutes** ⏱️

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/Saptha-me/create-bindu-agent.git
```

### What Happens Next?

You'll be prompted for:
- **Project name** and **description**
- **Agent framework** (Agno, LangChain, CrewAI, etc.)
- **License type** (MIT, Apache, BSD, GPL, ISC)
- **Author details**

Then, **boom!** 💥 Your agent project is ready with:

```
your-agent/
├── agent_config.json          # Agent configuration with A2A/AP2/X402 settings
├── your_agent/
│   ├── main.py               # Your agent entry point (already Bindu-fied!)
│   └── __init__.py
├── skills/                   # Template for adding agent skills
├── tests/                    # Pre-configured pytest tests
├── pyproject.toml            # Dependencies managed by uv
├── Dockerfile                # Ready for containerization
├── .github/workflows/        # CI/CD pipelines
└── README.md                 # Complete setup instructions
```

### Run Your Agent Locally

```bash
cd your-agent
uv sync                       # Install dependencies
uv run python -m your_agent.main  # Start your agent server
```

**That's it!** Your agent is now live at `http://localhost:8030` and ready to communicate with other agents using A2A, AP2, and X402 protocols.

<br/>


## Why This Matters

**The Problem**: Building agents is easy. Making them talk to each other? That's the hard part.

**The Old Way**:
```python
# Write your agent logic
# Figure out API endpoints
# Implement authentication
# Add error handling
# Configure deployment
# Write protocol adapters for A2A, AP2, X402
# Set up monitoring
# ... 3 days later, maybe it works?
```

**The Bindu Way**:
```bash
uvx cookiecutter https://github.com/Saptha-me/create-bindu-agent.git
# Answer 4 prompts
# Done. Your agent speaks A2A, AP2, and X402.
```

<br/>


## Why Use this?

- **2-Minute Setup**: Answer simple questions, get a complete production ready agentic system.
- **Lightweight**: No boilerplate. No configuration hell.
- **Simple**: No complex setup. Just configure and get a fully deployable agent.
- **Secure**: Built-in authentication, error tracking, and monitoring.
- **Protocol-Ready**: Built-in support for A2A, AP2, and X402 — your agent speaks the universal language
- **Framework Agnostic**: Works with Agno, LangChain, CrewAI, LlamaIndex, FastAgent, and more
- **Production-Ready**: Includes CI/CD, testing, Docker, documentation, and deployment configs.
- **Observability**: Built-in support for Phoenix, Langfuse, and Jaeger.
- **Best Practices**: Pre-configured with ruff, mypy, pytest, pre-commit hooks, and code quality tools
- **Deploy Anywhere**: Your agent becomes a living server, ready to join the Internet of Agents

<br/>

## What You Get

This Cookiecutter template scaffolds a complete Bindu Agent project with everything you need:

- [uv](https://docs.astral.sh/uv/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [ty](https://docs.astral.sh/ty/)
- Publishing to [PyPI](https://pypi.org) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Containerization with [Docker](https://www.docker.com/) or [Podman](https://podman.io/)




<br/>

## How It Works

```bash
┌─────────────────────────────────────────────────────────────┐
│  1. Run cookiecutter  →  2. Answer prompts  →  3. Deploy!   │
└─────────────────────────────────────────────────────────────┘
                              ↓
        Your agent is now live and speaking A2A, AP2, X402
                              ↓
              Ready to join the Internet of Agents 🌐
```

<br/>

### The Magic Behind the Scenes

When you create a Bindu Agent, you're not just getting a template — you're getting a **living server** that:

- **Speaks Universal Protocols**: A2A for agent-to-agent communication, AP2 for agentic commerce, X402 for payment rails
- **Secure by Design**: Built-in authentication, error tracking, and monitoring
- **Discoverable**: Your agent can be found and connected by other agents across the web
- **Framework Flexible**: Bring your own agent framework (Agno, LangChain, CrewAI, etc.)
- **Production-Ready**: From localhost to cloud in minutes, not days

<br/>

### The Vision

```bash
a peek into the night sky
}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
{{            +             +                  +   @          {{
}}   |                *           o     +                .    }}
{{  -O-    o               .               .          +       {{
}}   |                    _,.-----.,_         o    |          }}
{{           +    *    .-'.         .'-.          -O-         {{
}}      *            .'.-'   .---.   `'.'.         |     *    }}
{{ .                /_.-'   /     \   .'-.\                   {{
}}         ' -=*<  |-._.-  |   @   |   '-._|  >*=-    .     + }}
{{ -- )--           \`-.    \     /    .-'/                   {{
}}       *     +     `.'.    '---'    .'.'    +       o       }}
{{                  .  '-._         _.-'  .                   {{
}}         |               `~~~~~~~`       - --===D       @   }}
{{   o    -O-      *   .                  *        +          {{
}}         |                      +         .            +    }}
{{ jgs          .     @      o                        *       {{
}}       o                          *          o           .  }}
{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
```

Each symbol is an agent — a spark of intelligence.
And the single tiny dot is Bindu, the origin point in the Internet of Agents.<br/>

<br/>



## The Internet of Agents

Your Bindu Agent isn't just another API — it's a **citizen of the Internet of Agents**:

- **A2A (Agent-to-Agent)**: Seamless communication between AI agents
- **AP2 (Agentic Protocol 2)**: Commerce and transaction capabilities for agents
- **X402 (Payment Protocol)**: Built-in payment rails for agent services

Each protocol is pre-configured in your `agent_config.json`. Your agent speaks the universal language from day one.

<br/>

## Learn More

- **[Bindu Documentation](https://docs.saptha.me)** - Deep dive into Bindu's capabilities
- **[Bindu GitHub](https://github.com/Saptha-me/Bindu)** - The core library that powers your agent
- **[Join Discord](https://discord.gg/3w5zuYUuwt)** - Get help, share ideas, and connect with the community
- **[Example Agents](https://github.com/Saptha-me/Bindu/tree/main/examples)** - See Bindu agents in action

<br/>

## Built for the Future

We're entering the age of **agent swarms** — where thousands of AI agents collaborate, negotiate, and transact. Bindu ensures your agent is ready for this future:

- **Interoperable**: Works with any agent framework
- **Standards-Compliant**: A2A, AP2, X402 protocols built-in
- **Production-Grade**: Not a toy, not a demo — real infrastructure
- **Community-Driven**: Join the movement at [Saptha.me](https://saptha.me)

<br/>

## Contributing

We 💛 contributions! Whether you're:
- Adding new agent framework templates
- Improving documentation
- Fixing bugs
- Sharing your Bindu agent creations

Check out our [Contributing Guidelines](CONTRIBUTING.md) and join us on [Discord](https://discord.gg/3w5zuYUuwt)!

<br/>

## Acknowledgements

This project is partially based on [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv/tree/main)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Saptha-me/create-bindu-agent&type=date&legend=top-left)](https://www.star-history.com/#Saptha-me/create-bindu-agent&type=date&legend=top-left)

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>From idea to Internet of Agents in 2 minutes.</strong><br/>
  <em>Your agent. Your framework. Universal protocols.</em>
</p>

<p align="center">
  <a href="https://github.com/Saptha-me/create-bindu-agent">⭐ Star us on GitHub</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://docs.saptha.me">📚 Read the Docs</a>
</p>