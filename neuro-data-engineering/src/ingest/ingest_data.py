import pyspark.sql as spark
import requests
import os

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from API: {response.status_code}")

def load_local_data(file_path):
    if os.path.exists(file_path):
        return spark.read.csv(file_path, header=True, inferSchema=True)
    else:
        raise FileNotFoundError(f"Local data file not found: {file_path}")

def ingest_data(source_type, source):
    if source_type == 'api':
        return fetch_data_from_api(source)
    elif source_type == 'local':
        return load_local_data(source)
    else:
        raise ValueError("Invalid source type. Use 'api' or 'local'.")