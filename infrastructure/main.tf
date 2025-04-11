terraform {
  backend "s3" {
    bucket         = "ubicatech-tf-state-bucket" # local.bucket_name value
    key            = "tf-infra/terraform.tfstate"
    region         = "us-east-1" # local.aws_region value
    dynamodb_table = "ubicatech-tf-state-lock-table" # local.table_name value
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.94.1"
    }
  }
}

# Enable only on case of full destruction of the infrastructure
# module "tf-state" {
#   source      = "./modules/tf-state"
#   bucket_name = local.bucket_name
#   table_name  = local.table_name
# }

module "ccVPC" {
  source = "./modules/vpc"

  vpc_cidr             = local.vpc_cidr
  availability_zones   = local.availability_zones
  public_subnet_cidrs  = local.public_subnet_cidrs
  private_subnet_cidrs = local.private_subnet_cidrs
}

module "ecrRepo" {
  source = "./modules/ecr"

  ecr_repo_name = local.ecr_repo_name
}

module "db" {
  source = "./modules/db"

  cc_vpc_id               = module.ccVPC.vpc_id
  cc_private_subnets      = module.ccVPC.private_subnets
  cc_private_subnet_cidrs = local.private_subnet_cidrs

  db_az            = local.availability_zones[0]
  db_name          = local.db_name
  db_username      = local.db_username
}

module "migration" {
  source = "./modules/migration"

  cc_vpc_id         = module.ccVPC.vpc_id
  cc_public_subnets = module.ccVPC.public_subnets
  rds_instance_url  = "postgresql://${module.db.rds_credentials}@${module.db.rds_endpoint}"
  git_repo_url      = local.git_repo_url
  git_repo_branch   = local.git_repo_branch
}

provider "aws" {
  region = local.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}