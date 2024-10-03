# Configure the Linode provider
terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "~> 1.28.0"
    }
  }
}

# Set the provider
provider "linode" {
  token = var.linode_api_token
}

# Define variables
variable "linode_api_token" {
  description = "Your Linode API token"
  sensitive   = true
}

variable "root_pass" {
  description = "Root password for the Linode instance"
  sensitive   = true
}

variable "ssh_key" {
  description = "Public SSH key for accessing the Linode instance"
}

variable "docker_image" {
  description = "Docker image to deploy"
}

# Create a Linode instance
resource "linode_instance" "gpu_instance" {
  label           = "gpu-docker-instance"
  image           = "linode/ubuntu22.04"
  region          = "us-ord1"
  type            = "g6-standard-2"  # This is a GPU instance type
  authorized_keys = [var.ssh_key]
  root_pass       = var.root_pass

  # Install Docker and run the container
  provisioner "remote-exec" {
    inline = [
      "apt-get update",
      "apt-get install -y docker.io",
      "systemctl start docker",
      "systemctl enable docker",
      "docker pull ${var.docker_image}",
      "docker run -d ${var.docker_image}"
    ]
  }
}

# Output the instance IP
output "instance_ip" {
  value = linode_instance.gpu_instance.ip_address
}