# etl_covid_pipeline


![etl_pipeline](https://github.com/Chichi126/etl_covid_pipeline/assets/140970592/1f3fb8b0-0930-4bf7-9b87-16e0dd776bdc)



This repository contains an ETL (Extract, Transform, Load) data pipeline for gathering COVID-19 data from various sources, transforming it, and loading it into an AWS data warehouse. We’ll use Python, Airflow, Docker, and Terraform to orchestrate the entire process.

Project Structure

/src: Contains Python scripts for data extraction, transformation, and loading.

/airflow: Airflow DAGs for scheduling and orchestrating the pipeline.

/terraform: Infrastructure as Code (IaC) for setting up AWS services.

/docker: Dockerfiles for containerizing our Python scripts.

ETL Design

Extraction Layer:

Extract data from JHU, EDC, and OWID.

Store raw data in a staging area (e.g., S3 bucket).

Transformation Layer:

Clean, aggregate, and standardize data.

Calculate daily cases, deaths, and recovery rates.

Create a unified schema for all data sources.

Loading Layer:

Load transformed data into an RDS instance (our data warehouse).

Schedule the pipeline to run every 2 hours using Airflow.

How to Run

Setup AWS Services:

Use Terraform to create an S3 bucket, RDS instance, and necessary IAM roles.

Configure your AWS credentials.

Configure Airflow:

Install Airflow using pip install apache-airflow.

Set up your Airflow environment and configure DAGs in the /airflow directory.

Run the Pipeline:

Execute the Airflow DAG to trigger data extraction, transformation, and loading.

Monitor the progress in the Airflow UI.
