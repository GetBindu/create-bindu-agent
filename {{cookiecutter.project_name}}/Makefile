# ============================================================================
# SETUP & INSTALLATION
# ============================================================================

.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv sync
	@uv run pre-commit install

.PHONY: install-dev
install-dev: ## Install with development dependencies
	@echo "🚀 Installing development dependencies"
	@uv sync --all-extras
	@uv run pre-commit install

.PHONY: env-check
env-check: ## Check if required environment variables are set
	@echo "🔍 Checking environment variables..."
	@test -n "$$OPENROUTER_API_KEY" || (echo "❌ OPENROUTER_API_KEY not set" && exit 1)
	@test -n "$$MEM0_API_KEY" || (echo "❌ MEM0_API_KEY not set" && exit 1)
	@echo "✅ Required environment variables are set"

.PHONY: env-setup
env-setup: ## Create .env file from .env.example
	@if [ ! -f .env ]; then \
		echo "📝 Creating .env from .env.example"; \
		cp .env.example .env; \
		echo "⚠️  Please edit .env and add your API keys"; \
	else \
		echo "✅ .env file already exists"; \
	fi

# ============================================================================
# CODE QUALITY & TESTING
# ============================================================================

.PHONY: format
format: ## Format code with ruff
	@echo "🎨 Formatting code"
	@uv run ruff format .
	@uv run ruff check --fix .

.PHONY: lint
lint: ## Lint code with ruff
	@echo "🔍 Linting code"
	@uv run ruff check .

.PHONY: check
check: ## Run code quality tools
	@echo "🚀 Checking lock file consistency with 'pyproject.toml'"
	@uv lock --locked
	@echo "🚀 Linting code: Running pre-commit"
	@uv run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@uv run mypy .

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml

.PHONY: test-cov
test-cov: ## Run tests with coverage report
	@echo "🚀 Running tests with coverage"
	@uv run pytest --cov --cov-report=html --cov-report=term
	@echo "📊 Coverage report generated in htmlcov/index.html"

# ============================================================================
# AGENT MANAGEMENT
# ============================================================================

.PHONY: run
run: env-check ## Run the agent locally
	@echo "🤖 Starting {{cookiecutter.project_name}}..."
	@uv run python -m {{cookiecutter.project_slug}}

.PHONY: run-dev
run-dev: ## Run the agent in development mode with auto-reload
	@echo "🤖 Starting {{cookiecutter.project_name}} in development mode..."
	@uv run watchfiles "python -m {{cookiecutter.project_slug}}" {{cookiecutter.project_slug}}/

.PHONY: health
health: ## Check agent health
	@echo "🏥 Checking agent health..."
	@curl -f http://localhost:3773/health || echo "❌ Agent is not running"

# ============================================================================
# DOCKER COMMANDS
# ============================================================================

.PHONY: docker-build
docker-build: ## Build Docker image
	@echo "🐳 Building Docker image..."
	@docker build -f Dockerfile.agent -t {{cookiecutter.project_slug}}:latest .

.PHONY: docker-build-no-cache
docker-build-no-cache: ## Build Docker image without cache
	@echo "🐳 Building Docker image (no cache)..."
	@docker build --no-cache -f Dockerfile.agent -t {{cookiecutter.project_slug}}:latest .

.PHONY: docker-run
docker-run: ## Run Docker container with .env file
	@echo "🐳 Running Docker container..."
	@docker run -d \
		--name {{cookiecutter.project_slug}} \
		-p 3773:3773 \
		--env-file .env \
		--restart unless-stopped \
		{{cookiecutter.project_slug}}:latest
	@echo "✅ Container started. Check logs with: make docker-logs"

.PHONY: docker-run-it
docker-run-it: ## Run Docker container interactively
	@echo "🐳 Running Docker container (interactive)..."
	@docker run -it --rm \
		--name {{cookiecutter.project_slug}} \
		-p 3773:3773 \
		--env-file .env \
		{{cookiecutter.project_slug}}:latest

.PHONY: docker-stop
docker-stop: ## Stop Docker container
	@echo "🛑 Stopping Docker container..."
	@docker stop {{cookiecutter.project_slug}} || true
	@echo "✅ Container stopped"

.PHONY: docker-rm
docker-rm: docker-stop ## Remove Docker container
	@echo "🗑️  Removing Docker container..."
	@docker rm {{cookiecutter.project_slug}} || true
	@echo "✅ Container removed"

.PHONY: docker-logs
docker-logs: ## View Docker container logs
	@docker logs -f {{cookiecutter.project_slug}}

.PHONY: docker-shell
docker-shell: ## Open shell in running Docker container
	@docker exec -it {{cookiecutter.project_slug}} bash

.PHONY: docker-restart
docker-restart: docker-stop docker-run ## Restart Docker container

.PHONY: docker-clean
docker-clean: docker-rm ## Clean up Docker images and containers
	@echo "🧹 Cleaning up Docker resources..."
	@docker rmi {{cookiecutter.project_slug}}:latest || true
	@echo "✅ Docker cleanup complete"

# ============================================================================
# DOCKER COMPOSE COMMANDS
# ============================================================================

.PHONY: up
up: ## Start services with docker-compose
	@echo "🚀 Starting services with docker-compose..."
	@docker compose up -d
	@echo "✅ Services started. Check logs with: make logs"

.PHONY: up-build
up-build: ## Build and start services with docker-compose
	@echo "🚀 Building and starting services..."
	@docker compose up -d --build
	@echo "✅ Services started"

.PHONY: down
down: ## Stop and remove docker-compose services
	@echo "🛑 Stopping services..."
	@docker compose down
	@echo "✅ Services stopped"

.PHONY: logs
logs: ## View docker-compose logs
	@docker compose logs -f

.PHONY: ps
ps: ## List docker-compose services
	@docker compose ps

.PHONY: restart
restart: down up ## Restart docker-compose services

# ============================================================================
# BUILD & DEPLOYMENT
# ============================================================================

.PHONY: build
build: clean-build ## Build wheel file
	@echo "🚀 Creating wheel file"
	@uvx --from build pyproject-build --installer uv

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "🚀 Removing build artifacts"
	@uv run python -c "import shutil; import os; shutil.rmtree('dist') if os.path.exists('dist') else None"

.PHONY: docker-push
docker-push: ## Push Docker image to Docker Hub
	@echo "🚀 Pushing Docker image to Docker Hub..."
	@docker tag {{cookiecutter.project_slug}}:latest {{cookiecutter.dockerhub_username}}/{{cookiecutter.project_slug}}:latest
	@docker push {{cookiecutter.dockerhub_username}}/{{cookiecutter.project_slug}}:latest
	@echo "✅ Image pushed to Docker Hub"

.PHONY: docker-build-push
docker-build-push: docker-build docker-push ## Build and push Docker image

# ============================================================================
# DOCUMENTATION
# ============================================================================

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@uv run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@uv run mkdocs serve

.PHONY: docs-build
docs-build: ## Build documentation
	@uv run mkdocs build

# ============================================================================
# CLEANUP
# ============================================================================

.PHONY: clean
clean: clean-build ## Clean all generated files
	@echo "🧹 Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@rm -rf htmlcov/ .coverage coverage.xml
	@echo "✅ Cleanup complete"

.PHONY: clean-all
clean-all: clean docker-clean ## Clean everything including Docker resources

# ============================================================================
# UTILITY
# ============================================================================

.PHONY: version
version: ## Show version information
	@echo "📦 Package version:"
	@cat .version 2>/dev/null || echo "Version file not found"
	@echo "\n🐍 Python version:"
	@python --version
	@echo "\n📦 UV version:"
	@uv --version

.PHONY: status
status: ## Show agent and Docker status
	@echo "🔍 Agent Status:"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Docker Containers:"
	@docker ps -a | grep {{cookiecutter.project_slug}} || echo "No containers found"
	@echo "\nDocker Images:"
	@docker images | grep {{cookiecutter.project_slug}} || echo "No images found"
	@echo "\nAgent Health:"
	@curl -s http://localhost:{{cookiecutter._deployment_port}}/health 2>/dev/null | jq . || echo "Agent not responding"

.PHONY: help
help:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  📚 Makefile Commands"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

.DEFAULT_GOAL := help
