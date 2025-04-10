/* terraform {
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

module "tf-state" {
  source      = "./modules/tf-state"
  bucket_name = local.bucket_name
  table_name  = local.table_name
}

module "ubicatechVPC" {
  source = "./modules/vpc"

  vpc_cidr             = local.vpc_cidr
  vpc_tags             = var.vpc_tags
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

  cc_vpc_id               = module.ubicatechVPC.vpc_id
  cc_private_subnets      = module.ubicatechVPC.private_subnets
  cc_private_subnet_cidrs = local.private_subnet_cidrs

  db_az            = local.availability_zones[0]
  db_name          = "ccDatabaseInstance"
  db_user_name     = var.db_user_name
  db_user_password = var.db_user_password
}

module "migration" {
  source = "./modules/migration"

  cc_vpc_id         = module.ubicatechVPC.vpc_id
  cc_public_subnets = module.ubicatechVPC.public_subnets
}
 */

#Preparativos finales para el proyecto de terraform
terraform {
  required_version = "~> 1.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "ubicatech" {
  cidr_block = "10.0.0.0/16"
  tags ={
    Name = "ubicatech-vpc"
    project = "ubicatech"
  }
}