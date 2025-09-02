output "ec2_instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.atlas_migration.id
}
