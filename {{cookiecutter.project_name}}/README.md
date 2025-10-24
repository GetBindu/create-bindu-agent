<p align="center">
  <img src="https://raw.githubusercontent.com/Saptha-me/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> {{cookiecutter.project_name}} 🌻</h1>

<br/>

[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

<br/>

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation**: <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

<br/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.


<br/>

# From Zero to Production-Ready Agent in 2 Minutes

**[Create Bindu Agent](https://github.com/Saptha-me/create-bindu-agent/tree/main)** is the fastest way to build production-ready AI agents that speak the language of the Internet of Agents. No boilerplate. No configuration hell. Just configure and get a fully deployable agent that communicates using **A2A**, **AP2**, and **X402** protocols.

<br/>

## Quickstart

**Time to first agent: ~2 minutes** ⏱️

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/Saptha-me/create-bindu-agent.git
```

<br/>

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
