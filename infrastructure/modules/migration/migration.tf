resource "aws_security_group" "ccMigrationSecurityGroup" {
  name        = "allow_ssh_http"
  description = "Allow ssh http inbound traffic"
  vpc_id      = var.cc_vpc_id

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value["port"]
      to_port     = ingress.value["port"]
      protocol    = ingress.value["proto"]
      cidr_blocks = ingress.value["cidr_blocks"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "atlas_migration" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t2.micro"
  subnet_id                   = var.cc_public_subnets[0].id
  security_groups             = [aws_security_group.ccMigrationSecurityGroup.id]
  associate_public_ip_address = true

  user_data = <<-EOF
              #!/bin/bash -xe
              curl -sSfL https://atlasgo.sh -o install.sh
              chmod +x install.sh
              ./install.sh
              git clone -n --depth=1 --no-single-branch --filter=tree:0 ${var.git_repo_url}
              cd py-ubicatech
              git sparse-checkout set --no-cone /migrations
              git checkout ${var.git_repo_branch}
              atlas --config file://migrations/atlas/atlas.hcl --env tf --url ${var.rds_instance_url} migrate apply
              EOF
}
