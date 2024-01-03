# Paul-Emploi-Jed02
# Paul Emploi will help you know about the top X skills (technical or non-technical) needed for a given job. 

## Objectives

Build an ETL that includes takes data from pole emploie, extract info from it and save them to BigQuery

```python
import pandas as pd
from google.cloud import bigquery
from jobs import get_jobs
from processing import process_job_description
from dotenv import load_dotenv

load_dotenv()
# Define your dbt model (e.g., in a .sql file)

# Extract Data from Pôle Emploi API
def extract_data_from_pole_emploi(params: dict):
    # Convert the response to JSON
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    access_token = get_token(client_id = CLIENT_ID , client_secret = CLIENT_SECRET)
    data = get_jobs(params=params, access_token=access_token)
    return data

# Transform Data
def transform_data(params, data):
    # Convert data to DataFrame for easier manipulation

    # Keep only few columns

    #Keep only few records

    processed_jobs_list = []
    #For each of the few records, process the description and append the result to a list of dicts
    for job in limited_jobs:
        job_data = {}
        #fill the empty dict jobdata
        #include params in the dict
        #process description

    #append the dict to the list
    processed_jobs_list.append(job_data)
    
    #turn list into df 
    df_processed_jobs = #
    return df_processed_jobs

# Load Data to BigQuery
def load_data_to_bigquery(df, bigquery_client, dataset_id, table_id):
    # Specify the BigQuery dataset and table
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)

    # Load the DataFrame to BigQuery
    job = bigquery_client.load_table_from_dataframe(df, table_ref)
    job.result()  # Wait for the job to complete

    return job

# Main ETL Function
def etl_pipeline(params, bigquery_client, dataset_id, table_id):
    # Extract
    raw_data = extract_data_from_pole_emploi(api_url, api_key)

    # Transform
    transformed_data = transform_data(raw_data)

    # Load
    load_job = load_data_to_bigquery(transformed_data, bigquery_client, dataset_id, table_id)
    
    if load_job.state == 'DONE':
        print("Data successfully loaded to BigQuery.")
    else:
        print("Data load failed.")

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# Run the ETL pipeline
etl_pipeline({"domaine": "M18","motsCle": "data"}, bigquery_client, 'bq_dataset_id', 'paul_jobs_skills')
```