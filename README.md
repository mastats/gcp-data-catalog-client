# gcp-data-catalog-client
Client to manage tags using the GCP data_catalog client

This can be used at the end of a DAG in Airflow as a task to add Tags. 
Functionalities:
1. Add a Tag instance to a BigQuery table using an existing Tag Template
2. Update a table Tag instance. E.g. add more fields or delete existing ones
3. Get Tags fields assigned to a table for a specific Tag Template

Examples:
```
def hello_world():
    print("Hello, world!")
```
