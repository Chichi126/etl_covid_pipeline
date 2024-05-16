resource "random_password" "rdsword_pass" {
  length           = 24
  special          = false

}
resource "aws_ssm_parameter" "covidpass" {
  name  = "covid-password"
  type  = "String"
  value = random_password.rdsword_pass.result
}


module "covidrds" {
  source = "./module/datawarehouse"
  db_name = "chicoviddataset"
  identifier = "core-data-engineer"
  db_password = aws_ssm_parameter.covidpass.value
  db_username = "mytest"
}