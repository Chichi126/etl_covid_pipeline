resource "aws_s3_bucket" "covid_bucket" {
  bucket = var.bucket_name
}