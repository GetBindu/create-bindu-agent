<p align="center">
  <img src="assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> Create Bindu Agent 🌻</h1>

<p align="center">
  <em>"We imagine a world of agents where they can communicate with each other seamlessly.<br/>
  And Bindu turns your agent into a living server, the dot (Bindu) in the Internet of Agents."</em>
</p>

<style>
  .md-content__button {
    display: none;
  }
</style>

---

## From Zero to Production-Ready Agent in 2 Minutes

**Create Bindu Agent** is the fastest way to build production-ready AI agents that speak the language of the Internet of Agents. No boilerplate. No configuration hell. Just configure and get a fully deployable agent that communicates using **A2A**, **AP2**, and **X402** protocols.

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
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

## Why Use This?

- **2-Minute Setup**: Answer simple questions, get a complete production ready agentic system
- **Protocol-Ready**: Built-in support for A2A, AP2, and X402 — your agent speaks the universal language
- **Framework Agnostic**: Works with Agno, LangChain, CrewAI, LlamaIndex, FastAgent, and more
- **Production-Ready**: Includes CI/CD, testing, Docker, documentation, and deployment configs
- **Secure**: Built-in authentication, error tracking, and monitoring
- **Deploy Anywhere**: Your agent becomes a living server, ready to join the Internet of Agents

An example of a repository generated with this package can be found [here](https://github.com/getbindu/create-bindu-agent-example).

## Quickstart

**Time to first agent: ~2 minutes** ⏱️

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

### What Happens Next?

You'll be prompted for:
- **Project name** and **description**
- **Agent framework** (Agno, LangChain, CrewAI, etc.)
- **License type** (MIT, Apache, BSD, GPL, ISC)
- **Author details**

Then, **boom!** 💥 Your agent project is ready with a complete structure including agent configuration, tests, CI/CD pipelines, and more.

### Run Your Agent Locally

```bash
cd your-agent
uv sync                       # Install dependencies
uv run python -m your_agent.main  # Start your agent server
```

**That's it!** Your agent is now live at `http://localhost:8030` and ready to communicate with other agents using A2A, AP2, and X402 protocols.

For detailed setup instructions, navigate into your newly created project directory and follow the instructions in the `README.md`.

## The Internet of Agents

Your Bindu Agent isn't just another API — it's a **citizen of the Internet of Agents**:

- **A2A (Agent-to-Agent)**: Seamless communication between AI agents
- **AP2 (Agentic Protocol 2)**: Commerce and transactions between agents
- **X402 (Payment Rails)**: Decentralized payment infrastructure for agent economies

We're entering the age of **agent swarms** — where thousands of AI agents collaborate, negotiate, and transact. Bindu ensures your agent is ready for this future.

## Contributing

We 💛 contributions! Whether you're:
- Adding new agent framework templates
- Improving documentation
- Fixing bugs
- Sharing your Bindu agent creations

Check out our [Contributing Guidelines](https://github.com/getbindu/create-bindu-agent/blob/main/CONTRIBUTING.md) and join us on [Discord](https://discord.gg/3w5zuYUuwt)!

## Acknowledgements

This project is partially based on [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv) and [Audrey Feldroy's](https://github.com/audreyfeldroy) [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>From idea to Internet of Agents in 2 minutes.</strong><br/>
  <em>Your agent. Your framework. Universal protocols.</em>
</p>
