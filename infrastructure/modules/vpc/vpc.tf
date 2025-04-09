# Create a VPC
resource "aws_vpc" "ccVPC" {
  instance_tenancy = "default"
  cidr_block       = var.vpc_cidr
  tags             = var.vpc_tags
}

resource "aws_internet_gateway" "ccIGW" {
  vpc_id = aws_vpc.ccVPC.id
  tags = {
    Name    = "ccIGW"
    Project = "CC TF Demo"
  }
}
resource "aws_subnet" "ccPublicSubnet1" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.public_subnet_cidrs[0]
  availability_zone = var.availability_zones[0]
  tags = {
    Name    = "ccPublicSubnet1"
    Project = "CC TF Demo"
  }
}
resource "aws_subnet" "ccPublicSubnet2" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.public_subnet_cidrs[1]
  availability_zone = var.availability_zones[1]
  tags = {
    Name    = "ccPublicSubnet2"
    Project = "CC TF Demo"
  }
}

resource "aws_subnet" "ccPrivateSubnet1" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.private_subnet_cidrs[0]
  availability_zone = var.availability_zones[0]
  tags = {
    Name    = "ccPrivateSubnet1"
    Project = "CC TF Demo"
  }
}
resource "aws_subnet" "ccPrivateSubnet2" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.private_subnet_cidrs[1]
  availability_zone = var.availability_zones[1]
  tags = {
    Name    = "ccPrivateSubnet2"
    Project = "CC TF Demo"
  }
}

resource "aws_route_table" "ccPublicRT" {
  vpc_id = aws_vpc.ccVPC.id
  tags = {
    Name    = "ccPublicRT"
    Project = "CC TF Demo"
  }
}
resource "aws_route_table" "ccPrivateRT1" {
  vpc_id = aws_vpc.ccVPC.id
  tags = {
    Name    = "ccPrivateRT1"
    Project = "CC TF Demo"
  }
}

resource "aws_route_table_association" "ccPublicRTassociation1" {
  subnet_id      = aws_subnet.ccPublicSubnet1.id
  route_table_id = aws_route_table.ccPublicRT.id
}
resource "aws_route_table_association" "ccPublicRTassociation2" {
  subnet_id      = aws_subnet.ccPublicSubnet2.id
  route_table_id = aws_route_table.ccPublicRT.id
}
