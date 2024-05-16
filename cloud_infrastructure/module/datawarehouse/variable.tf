variable "allocated_storage" {
    default = "10"
    }

variable "engine_version" {
    default = "16.1"
}

variable "instance_class" {
    default = "db.t3.micro" 
}

variable "engine" {
    default = "postgres" 
}

variable "db_name" {}

variable "identifier" {}

variable "db_username" {}

variable "db_password" {}

