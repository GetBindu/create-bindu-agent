FROM node:22.12.0-slim AS builder

FROM python:3.12-slim

# OCI labels
LABEL org.opencontainers.image.title="{{cookiecutter.project_name}}"
LABEL org.opencontainers.image.description="{{cookiecutter.project_description}}"
LABEL org.opencontainers.image.authors="{{cookiecutter.author}} <{{cookiecutter.email}}>"
LABEL org.opencontainers.image.version="{{cookiecutter._agent_version}}"
LABEL org.opencontainers.image.source="https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}"
LABEL org.opencontainers.image.licenses="MIT"

ARG nodejs_canonical="22.12.0"

# Create non-root user
RUN groupadd -g 1000 bindu_user && useradd -u 1000 -g bindu_user -s /bin/bash -m bindu_user

# Copy Node.js from builder
COPY --from=builder /usr/local/bin/node /usr/local/bin/
COPY --from=builder /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm && \
    ln -s /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx

# Install Python tools
RUN pip install --no-cache-dir -U pip pipenv uv

WORKDIR /app

# Copy only the dist directory containing the built wheel
COPY dist/ ./dist/

# Install the package from the wheel file
RUN pip install --no-cache-dir ./dist/*.whl

# Set the user
USER bindu_user

# Expose the agent server port
EXPOSE 3773

# Run the application
CMD ["python", "-m", "{{cookiecutter.project_slug}}.main"]
