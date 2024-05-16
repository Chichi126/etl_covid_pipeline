# etl_covid_pipeline




![etl_pipeline](https://github.com/Chichi126/etl_covid_pipeline/assets/140970592/02077c88-43e5-4c1d-b6eb-1c268da7be92)




This repository contains an ETL (Extract, Transform, Load) data pipeline for gathering COVID-19 data from various sources, transforming it, and loading it into an AWS data warehouse. We’ll use Python, Airflow, Docker, and Terraform to orchestrate the entire process.

**Project Structure**

Contains Python scripts for data extraction, transformation, and loading.

**Airflow**: Airflow DAGs for scheduling and orchestrating the pipeline.

**Terraform**: Infrastructure as Code (IaC) for setting up AWS services.

**Airbyte**: Used to connect S3 bucket to the RDS

**Docker**: Dockerfiles for containerizing our Python scripts.

**ETL Design**

**Extraction Layer**:

Extract data from RapidAPI.

Store raw data in a staging area (e.g., S3 bucket).

**Transformation Layer**:

Clean, aggregate, and standardize data.


Create a unified schema for all data sources.

**Loading Layer**:

Load transformed data into an RDS instance (our data warehouse).

Schedule the pipeline to run every 2 hours using Airflow.


**Setup AWS Services**:

Use Terraform to create an S3 bucket, RDS instance, and necessary IAM roles.

Configure AWS credentials.

Configure Airflow:

Install Airflow using pip install apache-airflow.

Set up your Airflow environment and configure DAGs in the /airflow directory.

Configure Airbyte:

Set up the environment and use docker-compose up to start up the airbyte

Set up the source and destination, connect and synchronize ( for me my source was s3 and the destination was RDS)



**Run the Pipeline**:

Execute the Airflow DAG to trigger data extraction, transformation, and loading.

Monitor the progress in the Airflow UI.
