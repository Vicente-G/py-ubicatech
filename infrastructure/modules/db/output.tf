output "rds_endpoint" {
  value = aws_db_instance.ccRDS.endpoint
}
output "rds_credentials" {
  value     = "${aws_db_instance.ccRDS.username}:${random_password.password.result}"
  sensitive = true
}
