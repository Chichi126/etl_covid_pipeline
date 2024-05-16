resource "aws_db_instance" "de_bikesales" {
  allocated_storage    = var.allocated_storage
  db_name              = var.db_name
  identifier           = var.identifier
  engine               = var.engine
  engine_version       = var.engine_version
  instance_class       = var.instance_class
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
  publicly_accessible  = true
}

#remember to the de-bikesales