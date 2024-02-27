terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.18.0"
    }
  }
}

provider "google" {
  credentials = file(var.gcp_key)
  project = var.gcp_project
  location = var.gcp_region
}