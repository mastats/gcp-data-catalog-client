# gcp-data-catalog-client
* Client to manage tags using the GCP data_catalog client
* Interacting with the Data Catalog client requires a GCP service account key. Read this: https://cloud.google.com/iam/docs/keys-create-delete

## Usage
* Add & update BigQuery tables metadata. E.g. A task in an Airflow ETL DAG to add metadata about data ingestion or governance.
* Retrieve tags assigned to different tables and use metadata to build a report

### Basic usage
1. Add a Tag instance to a BigQuery table using an existing Tag Template
2. Update a table Tag instance. E.g. add more fields or delete existing ones
3. Get Tags fields assigned to a table for a specific Tag Template

### Example

```
# Create an instance of the TagClient class
tag_client = TagClient(
    project_id="project-id",
    dataset_id="dataset-id",
    table_id="table-id",
    location="tag-template-location",
    tag_template_id="tag-template-id",
    key_path="/path/to/key/file.json"
)

# Create a tag instance for the selected table
tag_instance = tag_client.create_tag_instance({
    "data_ingestion_owner": "John Doe",
    "rows_processed": 123,
    "pii": False,
    "final_report_name": sales_market_01
})

# Update table existing tag instance's fields
updated_tag_instance = tag_client.update_tag_instance({
    "field1": "new-value",
    "field2": 456
})

```




