resource "aws_vpc" "ccVPC" {
  instance_tenancy = "default"
  cidr_block       = var.vpc_cidr
}

resource "aws_internet_gateway" "ccIGW" {
  vpc_id = aws_vpc.ccVPC.id
}

resource "aws_subnet" "ccPublicSubnet1" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.public_subnet_cidrs[0]
  availability_zone = var.availability_zones[0]
}

resource "aws_subnet" "ccPublicSubnet2" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.public_subnet_cidrs[1]
  availability_zone = var.availability_zones[1]
}

resource "aws_subnet" "ccPrivateSubnet1" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.private_subnet_cidrs[0]
  availability_zone = var.availability_zones[0]
}

resource "aws_subnet" "ccPrivateSubnet2" {
  vpc_id            = aws_vpc.ccVPC.id
  cidr_block        = var.private_subnet_cidrs[1]
  availability_zone = var.availability_zones[1]
}

resource "aws_route_table" "ccPublicRT" {
  vpc_id = aws_vpc.ccVPC.id
}

resource "aws_route_table" "ccPrivateRT1" {
  vpc_id = aws_vpc.ccVPC.id
}

resource "aws_route_table_association" "ccPublicRTassociation1" {
  subnet_id      = aws_subnet.ccPublicSubnet1.id
  route_table_id = aws_route_table.ccPublicRT.id
}
resource "aws_route_table_association" "ccPublicRTassociation2" {
  subnet_id      = aws_subnet.ccPublicSubnet2.id
  route_table_id = aws_route_table.ccPublicRT.id
}
