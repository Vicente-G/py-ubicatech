# Change AMI variable using https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance

locals {
  ami_id        = "ami-026b57f3c383c2eec"
  instance_type = "t2.micro"
  key_name      = "ccKP"
}