# Bindu Agent Installer

Cross-platform installer scripts for Bindu AI agents.

## 🌻 Brew-Style Installation (Recommended)

Install Bindu agents with a single command:

### Linux/macOS
```bash
curl -fsSL getbindu.com/install.sh | bash
```

### Windows
```powershell
iwr -useb getbindu.com/install.ps1 | iex
```

## Files
- `install.sh` - Hosted installer (served from bindus.directory/public/)
- `install.cmd` - Windows installer (legacy, local use)

## Features

### 🎯 Smart Skill Selection
- **Categorized Skills**: Skills organized by domain (Business, Research, Creative, etc.)
- **Multi-Select**: Choose multiple skills across different categories
- **29 Pre-built Skills**: Finance, Research, Content Creation, Travel, Health, and more

### ⚙️ Framework Support
- Agno (Recommended)
- LangChain
- CrewAI
- FastAgent
- OpenAI Agent
- Google ADK Agent

### 🔐 Security & Auth
- DID & PKI support
- Auth0, Cognito, Azure AD, Google authentication
- Phoenix, Jaeger, Langfuse observability

### 🚀 Auto-Setup
- Fresh template clone each time
- Automatic dependency installation via `uv`
- GitHub Actions integration
- Docker support

## Installation Workflow

1. **System Check** - Verifies Git and uv installation
2. **Skill Selection** - Interactive categorized skill picker
3. **Agent Configuration** - Name, framework, auth, security options
4. **Generation** - Creates agent via cookiecutter
5. **Finalization** - Installs dependencies and prepares agent

## Skill Categories

- 💼 **Business & Finance** (5 skills)
- 🔬 **Research & Analysis** (4 skills)
- 🎨 **Creative & Content** (6 skills)
- 🌟 **Personal & Lifestyle** (5 skills)
- 💚 **Health & Wellness** (5 skills)
- ⚙️ **Technical & Development** (2 skills)
- ⚖️ **Legal & Compliance** (2 skills)

## Requirements
- Git
- Python 3.8+
- Internet connection
- uv (auto-installed if missing)

## Hosting

The installer is hosted at `getbindu.com/install.sh` via Vercel from the `bindus.directory` repository.

### Deployment
The `install.sh` file in `bindus.directory/public/` is automatically served by Vercel at the root domain.

## Local Development

To test the installer locally:

```bash
# Make executable
chmod +x install.sh

# Run directly
./install.sh

# Or via curl simulation
bash install.sh
```

## Troubleshooting
- Ensure Git is installed
- Check network connectivity
- Verify uv installation: `uv --version`
- For Windows, run PowerShell as Administrator if needed
