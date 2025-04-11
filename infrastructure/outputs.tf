output "aws_region" {
  value = local.aws_region
}

output "aws_access_key" {
  value = var.aws_access_key
  sensitive = true
}

output "aws_secret_key" {
  value = var.aws_secret_key
  sensitive = true
}

output "ec2_instance_id" {
  value = aws_instance.ccMigration.id
}

output "ecr_repo_url" {
  value = module.ecrRepo.ecr_repo_url
}

output "rds_instance_url" {
  value = "postgresql://${module.db.rds_credentials}@${module.db.rds_endpoint}"
  sensitive = true
}
