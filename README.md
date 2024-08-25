# python-vscode-dev

Use a VSCode dev container as your virtual Python development environment.

## Features

- Dockerized development environment and VSCode devcontainer setup
- Use `pip` to install Python packages
- Set environment variables in `.env` file

## Getting Started

### Prerequisites

- install [Docker](https://www.docker.com/get-started)
- install [VSCode](https://code.visualstudio.com/download)

### Customize your Python project

- set your env variables by copying `.env.example` to `.env` and fill in the values
- add your Python packages to `requirements.txt`

### Open your project in VSCode

```bash
ssh-add ~/.ssh/id_rsa   # to share your git credentials with container
code .                  # open project in VSCode
```

In VSCode, choose "Reopen in Container" to fire up container.

Open up a terminal in VSCode.

Run `env` to verify env vars look good.

`python app.py`
