# python-vscode-dev

Use a VSCode dev container as your virtual Python development environment.

Includes dependencies for LangChain, LangGraph, Juypter Notebook, and PyGraphviz (for visualization).

Example LangChain and LangGraph code.

Load environment variables via `.env` file.

## Getting Started

### Prerequisites

- install [Docker](https://www.docker.com/get-started)
- install [VSCode](https://code.visualstudio.com/download)

### Setup

- **Important: You must create an `.env` file by copying `.env.example` to `.env` and filling in the values for the dev container to run**
- add your Python packages to `requirements.txt`

### Open your project in VSCode

```bash
ssh-add ~/.ssh/id_rsa   # to share your git credentials with container
code .                  # open project in VSCode
```

In VSCode, choose "Reopen in Container" to fire up container. Ensure you setup an `.env` file before launching dev container.

Open up a terminal in VSCode.

Run `env` to verify env vars look good.

`python src/app.py`

## Running a Jupyter Notebook

In VSCode terminal, run `jupyter notebook --allow-root`. Open up a browser and navigate to the URL shown in terminal. `--allow-root` is fine since Python is running in a dev container.

In browser UI, create a new Python 3 notebook to get started.

If you copy in `app.py` into the notebook, you can run the code in the notebook and also see graphviz visualizations of the workflow.
