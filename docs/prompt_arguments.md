# Prompt arguments

When running the cookiecutter command, a prompt will start which enables you to configure your Bindu agent. The prompt values and their explanation are as follows:

---

## Basic Information

**author**

Your full name.

**email**

Your email address.

**author_github_handle**

Your GitHub handle, i.e. `<handle>` in `https://github.com/<handle>`

**project_name**

Your project name. Should be equal to the name of your repository and should only contain alphanumeric characters and `-`'s. Default: `my-bindu-agent`

**project_slug**

The project slug, will default to the `project_name` with all `-`'s replaced with `_`. This will be how you import your code later, e.g.

```python
from <project_slug> import handler
```

**project_description**

A short description of your agent project. Default: `A Bindu AI agent for intelligent task handling`

---

## Agent Configuration

**project_name**

The name of your agent project. Default: `my-bindu-agent`

**agent_version**

The initial version of your agent. Default: `1.0.0`

**bindu_version**

The Bindu framework version to use. Default: `0.3.18`

**agent_framework**

Choose your preferred agent framework:
- `agno` (default)
- `langchain`
- `crew`
- `fastagent`
- `openai agent`
- `google adk agent`
- `custom`

**include_example_skills**

`"y"` or `"n"`. Include example skills in your agent project.

**skill_names**

Comma-separated list of skill names to include. Default: `question-answering,pdf-processing`

---

## Security & Authentication

**enable_auth**

`"y"` or `"n"`. Enable authentication for your agent.

**auth_provider**

Choose your authentication provider:
- `auth0` (default)
- `cognito(not implemented)`
- `azure ad(not implemented)`
- `google(not implemented)`
- `custom(not implemented)`
- `none`

**enable_did**

`"y"` or `"n"`. Enable Decentralized Identifiers (DID) for your agent.

**enable_pki**

`"y"` or `"n"`. Enable Public Key Infrastructure (PKI) for secure communication.

**recreate_keys**

`"y"` or `"n"`. Recreate cryptographic keys on each deployment.

**verification_key_type**

Choose the cryptographic key type:
- `rsa` (default)
- `ecdsa`

---

## Agent Behavior

**enable_system_message**

`"y"` or `"n"`. Enable system messages for your agent.

**enable_context_based_history**

`"n"` or `"y"`. Enable context-based conversation history.

---

## Observability & Monitoring

**enable_telemetry**

`"y"` or `"n"`. Enable telemetry and tracing for your agent.

**enable_llm_observability**

`"y"` or `"n"`. Enable LLM-specific observability.

**llm_observability_provider**

Choose your LLM observability provider:
- `phoenix` (default)
- `langfuse`

**use_jaeger**

`"y"` or `"n"`. Use Jaeger for distributed tracing.

**log_level**

Set the logging level:
- `info` (default)
- `debug`
- `warning`
- `error`

---

## Storage & Scheduling

**storage_type**

Choose your storage backend:
- `memory` (default)
- `postgres(not implemented)`

**scheduler_type**

Choose your scheduler backend:
- `memory` (default)
- `redis(not implemented)`

---

## Deployment

**deployment_host**

The host address for your agent server. Default: `0.0.0.0`

**deployment_port**

The port for your agent server. Default: `3773`

---

## Development Tools

**type_checker**

Choose your type checker:
- `ty` (default) - Fast type checker from Astral
- `none`

**include_github_actions**

`"y"` or `"n"`. Adds a `.github` directory with various actions and workflows to setup the environment and run code formatting checks and tests.

**mkdocs**

`"y"` or `"n"`. Adds [MkDocs](https://www.mkdocs.org/) documentation to your project. This includes automatically parsing your docstrings and adding them to the documentation. Documentation will be deployed to the `gh-pages` branch.

**codecov**

`"y"` or `"n"`. Adds code coverage checks with [codecov](https://about.codecov.io/).

**dockerfile**

`"y"` or `"n"`. Adds a Dockerfile and docker-compose.yml for containerization.

**devcontainer**

`"n"` or `"y"`. Adds a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) specification to the project along with pre-installed pre-commit hooks and VSCode python extension configuration.

---

## License

**open_source_license**

Choose a [license](https://choosealicense.com/) for your project:
- `MIT license` (default)
- `Apache Software License 2.0`
- `BSD license`
- `ISC license`
- `GNU General Public License v3`
- `Not open source`

---
