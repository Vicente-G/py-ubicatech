# Ubica-tech's Python Project

The Ubica-tech team, has started the development of a Python API based on Flask and SQLModel.

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
- [Atlas](https://atlasgo.io/guides/evaluation/install)
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

3. Finally, create a `.env` file, for developing just use our example:
```sh
cp example.env .env
```

4. (Optional) Enable Git hooks for development:
```sh
uv run task githooks
```

## Usage

1. Run an SSL-enabled PostgreSQL instance, for example with docker:
```sh
docker run -d -p 5432:5432 --name pg17 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=ubicatech postgres:17.4 -c ssl=on -c ssl_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem -c ssl_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
```

2. Run the migration command, in this case, migrate locally with:
```sh
uv run task db-test
```

3. (Optional) Check more on the migration made using `\dt` on this client:
```sh
PGPASSWORD=postgres psql -h localhost -p 5432 -U postgres -w ubicatech
```
Or, check the schema with Atlas using its public webapp with this CLI command:
```sh
uv run task db-check
```

4. Finally, you can run the server with gunicorn using:
```sh
uv run task start
```

Additionally, to use any other command defined on the `pyproject.toml` file:
```sh
uv run task <command-name>
```
