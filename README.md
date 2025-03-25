# Ubica-tech's Python Project

The Ubica-tech team, has started the development of a Python API based on Flask and SQLAlchemy.

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
- [Terraform](https://developer.hashicorp.com/terraform/install)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide)
- [Jenkins](https://www.jenkins.io/doc/book/installing/)

## Installation

1. Clone the repository:
```sh
git clone https://github.com/SamuelPerez21/py-ubicatech.git
cd py-ubicatech
```

2. Sync environment with the lock-file:
```sh
uv sync
```

3. (Optional) Enable Git hooks for development:
```sh
uv run task githooks
```

## Usage

For launching the server in debug mode, run the following:
```sh
uv run task dev
```

In general, to use any other command defined on the `pyproject.toml` file:
```sh
uv run task <command-name>
```
