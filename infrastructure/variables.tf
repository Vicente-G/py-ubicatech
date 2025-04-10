variable "project_name" {
  description = "Nombre del proyecto"
  default     = "ubicatech"
}

variable "region" {
  default = "us-east-1"
}

variable "vpc_cidr" {
  default = "10.20.0.0/16"
}

variable "private_subnets" {
  type    = list(string)
  default = ["10.20.1.0/24", "10.20.2.0/24"]
}

variable "public_subnets" {
  type    = list(string)
  default = ["10.20.101.0/24", "10.20.102.0/24"]
}

variable "db_user" {}

variable "db_password" {}

variable "vpc_tags" {
  description = "Tags for VPC"
  type        = map(any)
}

variable "db_user_name" {
  description = "RDS DB User"
  type        = string
  sensitive   = true
  validation {
    condition     = length(var.db_user_name) > 5
    error_message = "DB UserName must not be empty."
  }
}

variable "db_user_password" {
  description = "RDS DB User Password"
  type        = string
  sensitive   = true
  validation {
    condition     = length(var.db_user_password) > 8
    error_message = "DB User Password must not be empty."
  }
}
