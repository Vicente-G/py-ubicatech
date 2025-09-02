locals {
  # Terraform's Backend
  bucket_name = "ubicatech-tf-state-bucket"
  table_name  = "ubicatech-tf-state-lock-table"

  # AWS Region
  aws_region = "us-east-1"

  # Database Configuration
  db_name     = "ubicatech"
  db_username = "ubicatech"

  # Git Repo Configuration
  git_repo_url    = "https://github.com/Vicente-G/py-ubicatech.git"
  git_repo_branch = "dev"

  # AWS ECR
  ecr_repo_name = "ubicatech/py-server"

  # VPC Configuration
  vpc_cidr             = "10.0.0.0/16"
  availability_zones   = ["us-east-1a", "us-east-1b"]
  public_subnet_cidrs  = ["10.0.0.0/24", "10.0.1.0/24"]
  private_subnet_cidrs = ["10.0.3.0/24", "10.0.4.0/24"]
}
