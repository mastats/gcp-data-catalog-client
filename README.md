# gcp-data-catalog-client
Client to manage tags using the GCP data_catalog client

## Usage
This can be used to add metadata to BigQuery tables at the beginning, during or at the end of the ETL process.
E.g. a task in Airflow to add metadata about data ingestion or governance.

## Basic usage
1. Add a Tag instance to a BigQuery table using an existing Tag Template
2. Update a table Tag instance. E.g. add more fields or delete existing ones
3. Get Tags fields assigned to a table for a specific Tag Template

## Examples

```
def hello_world():
    print("Hello, world!")
```
