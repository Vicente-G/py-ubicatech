# Infrastructure provisioning

A Terraform/Ansible pipeline to provision AWS with the infrastructure require to run SoloUno.

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Terraform](https://developer.hashicorp.com/terraform/install)

## Installation

1. Sync environment with the lock-file:
```sh
uv sync
```

2. Setup environment variables to be used on terraform's tfvars:
```sh
cp sample.terraform.tfvars terraform.tfvars
```

3. Initialize repo adding providers and module references:
```sh
uv run task compile
```

4. Configure the AWS CLI using the following command:
```sh
uv run task aws-config
```

## Usage

1. Run the terraform's provisioning planning with:
```sh
uv run task plan
```

2. Once everything seems okay, apply the provisioning over AWS:
```sh
uv run task apply
```

3. From the terraform's output put the variables into the environment.
Also add the ECR's password from the output of:
```sh
uv run task ecr-login
```

4. Run the post provisioning steps with Ansible using:
```sh
uv run task post-apply
```

At this point everything should be set and done on AWS!

5. (Optional) Remove all the infrastructure:
```sh
uv run task destroy
```