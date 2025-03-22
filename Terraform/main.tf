provider "aws" {
  region = "eu-north-1"
}

# Define an EC2 instance resource
resource "aws_instance" "example" {
  ami           = "ami-0c1ac8a41498c1a9c"
  instance_type = "t3.micro"
  tags = {
    Name = "MyFirstInstanceUsingTerraform"
  }
}

output "instance_public_ip" {
  value = aws_instance.example.public_ip
}

