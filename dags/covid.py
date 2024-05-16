import requests
import json
import pandas as pd
import awswrangler as wr
from path_chi import s3_mydest, s3_clean


def extract_data():
    with open(r'dags/config_api.json', 'r') as api_key:
        my_apikey = json.load(api_key)
        s3_path = s3_mydest()  # Make sure this is correct

    # Debug: Print or log the type and value of s3_path
    print(f"s3_path type: {type(s3_path)}, s3_path value: {s3_path}")

    headers = my_apikey
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"dataset not found due to status_code: {response.status_code}")
    else:
        raw_data = response.json()

        for i in raw_data['response']:
            data.append(i)
        df = pd.DataFrame.from_records(data)
        wr.s3.to_parquet(df=df, path=s3_path)
        return df

extract_data()


def clean_data():
    df = extract_data()
    active_values = []
    one_million_population = []
    total = []
    s3_path = s3_clean()

    for i, row in df.iterrows():
        if isinstance(row['cases'], dict):
            active_values.append(row['cases'].get('active'))
        else:
            active_values.append(None)
            
        if isinstance(row['deaths'], dict):
            one_million_population.append(row['deaths'].get('1M_pop'))
        else:
            one_million_population.append(None)

        if isinstance(row['deaths'], dict):
            total.append(row['deaths'].get('totals'))
        else:
            total.append(None)

    # Add the extracted columns to the DataFrame
    df['active'] = active_values
    df['one_million_pop'] = one_million_population
    df['totals'] = total

    # Drop the unwanted columns
    df.drop(columns=['cases', 'deaths'], inplace=True)
    wr.s3.to_parquet(df=df, path=s3_path)

    return df
clean_data()


import boto3
import psycopg2

# AWS credentials and region
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
region_name = 'YOUR_AWS_REGION'

# S3 bucket and file details
bucket_name = 'YOUR_S3_BUCKET_NAME'
file_key = 'YOUR_FILE_KEY'

# RDS connection details
db_host = 'YOUR_RDS_HOST'
db_port = 'YOUR_RDS_PORT'
db_name = 'YOUR_DATABASE_NAME'
db_user = 'YOUR_DATABASE_USERNAME'
db_password = 'YOUR_DATABASE_PASSWORD'

# Initialize S3 and RDS clients
s3 = boto3.client('s3', region_name=region_name,
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Download file from S3
local_file_path = 'file.csv'
s3.download_file(bucket_name, file_key, local_file_path)

# Connect to PostgreSQL RDS instance
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Load data from the CSV file into a table (replace table_name and column_names with your actual table and column names)
with open(local_file_path, 'r') as f:
    next(f)  # Skip the header row if it exists
    cur.copy_from(f, 'table_name', sep=',', columns=('column1', 'column2', ...))

# Commit the transaction
conn.commit()

# Close communication with the database
cur.close()
conn.close()
