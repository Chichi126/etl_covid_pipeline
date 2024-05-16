from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.transfers.s3_to_s3 import S3ToS3Operator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from covid import extract_data, clean_data


default_args = {
    'owner': 'chi_project',
    'email': ['chinyere.nwigwe126@gmail.com'],
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 15),
    'retries': 5,
    'retry_delay': timedelta(seconds=10),
    'execution_timeout': timedelta(minutes=10)
}


dag = DAG(
    dag_id="chi_covid",
    default_args=default_args,
    description='de intentional',
    schedule_interval="0 * * * *",
    max_active_runs=1,
    catchup=False
)


extract_zillow_data = PythonOperator(
    task_id="to_extract_data",
    dag=dag,
    python_callable= extract_data
        )

clean_data_task = PythonOperator(
    task_id='my_clean_data',
    python_callable=clean_data,
    op_args=[extract_data.output],
    provide_context=True,
    dag=dag,
)

transfer_to_athena_task = S3ToAthenaOperator(
    task_id='transfer_to_athena',
    s3_bucket='chicovid',
    s3_key='covid_cleaned_dataset.parquet ',
    database='your_athena_database',
    table='cleaned_data',
    dag=dag,
)



transfer_to_redshift_task = S3ToRedshiftOperator(
    task_id='transfer_to_redshift',
    schema='public',
    table='cleaned_data',
    s3_bucket='chicovid',
    s3_key='covid_cleaned_dataset.parquet',
    redshift_conn_id='your_redshift_connection_id',
    aws_conn_id='your_aws_connection_id',
    dag=dag,
)
