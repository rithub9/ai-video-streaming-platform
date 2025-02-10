provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "video_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_eks_cluster" "video_cluster" {
  name     = "ai-video-cluster"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = ["subnet-12345", "subnet-67890"]
  }
}
