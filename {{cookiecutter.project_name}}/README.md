<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">{{cookiecutter.project_name}}</h1>
<h3 align="center">{{cookiecutter.project_description}}</h3>

<p align="center">
  <strong>{{cookiecutter.project_description}}</strong><br/>
  {{cookiecutter.project_description}}
</p>

<p align="center">
  [![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
  [![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
  [![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
</p>

---

## 🚀 What Makes This Special?

**Stop endless scrolling.** This AI agent understands what you *actually* want:

**Perfect for:** {{cookiecutter.project_description}}

---

## 📚 Quick Links

- 📖 **[Full Documentation](https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/)**
- 💻 **[GitHub Repository](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/)**
- 🐛 **[Report Issues](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/issues)**
- 💬 **[Join Discord](https://discord.gg/3w5zuYUuwt)**

<br/>

## ⚡ Quick Start (5 Minutes)

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (fast Python package installer)
- API keys (free tiers available)

### 1️⃣ Clone & Install

```bash
# Clone the repository
git clone https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
cd {{cookiecutter.project_name}}

# Install dependencies + pre-commit hooks
make install
```

### 2️⃣ Configure API Keys

```bash
# Copy environment template
cp .env.example .env
```

Edit `.env` and add your keys:

| Key | Get It From | Free Tier? |
|-----|-------------|------------|
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Yes |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | ✅ Yes |

### 3️⃣ Run Your Agent

```bash
# Start the agent
make run

# Or use Docker
docker-compose up
```

**That's it!** 🎉 Your AI travel agent is live.

---

## 💡 Usage Examples

Try these queries:

```python
# Natural language search
{{cookiecutter.project_description}}
```

---

## 🛠️ Development Setup

### Running Tests

```bash
make test              # Run all tests
make test-cov          # With coverage report
```

### Code Quality

```bash
make format            # Format code
make lint              # Run linters
make check             # Format + lint + test
```

### Pre-commit Hooks

Fix formatting issues before committing:

```bash
uv run pre-commit run -a
```

---

## 🐳 Docker Deployment

### Local Docker

```bash
# Build and run
docker-compose up --build

# Production mode
docker-compose -f docker-compose.prod.yml up
```

### Docker Hub Auto-Deploy

Enable automatic Docker image publishing:

1. Go to **Settings → Secrets → Actions**
2. Add secret: `DOCKERHUB_TOKEN` (get from [Docker Hub](https://hub.docker.com/settings/security))
3. Push to `main` → Image auto-builds and publishes 🚀

---

## 🏗️ Project Structure

```
{{cookiecutter.project_name}}/
├── {{cookiecutter.project_slug}}/    # Main agent code
│   ├── skills/             # Agent capabilities
│   │   └── {{cookiecutter.project_slug}}/ # {{cookiecutter.project_name}} skill
│   └── __init__.py
├── tests/                  # Test suite
├── docs/                   # Documentation
├── .env.example            # Environment template
├── docker-compose.yml      # Docker setup
└── pyproject.toml          # Dependencies
```


<br/>

## 🌟 Contributing

We love contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

**Built with [Bindu Agent Framework](https://github.com/getbindu/bindu)**

- 🌐 **A2A, AP2, X402 protocols** for Internet of Agents communication
- ⚡ **Zero-config setup** - from idea to production in minutes
- 🛠️ **Production-ready** out of the box

### Want to Build Your Own Agent?

```bash
# Create a new agent in 2 minutes
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/raahulrahl/airbnb-travel-agent">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://docs.getbindu.com">📚 Bindu Docs</a>
</p>

<p align="center">
  <em>From idea to Internet of Agents in minutes. 🌻🚀✨</em>
</p>
