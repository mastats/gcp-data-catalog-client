# gcp-data-catalog-client
Client to manage tags using the GCP data_catalog client

## Usage
1. Add & update BigQuery tables metadata. E.g. A task in an Airflow ETL DAG to add metadata about data ingestion or governance.
2. Retrieve tags assigned to different tables and use metadata to build a report

### Basic usage
1. Add a Tag instance to a BigQuery table using an existing Tag Template
2. Update a table Tag instance. E.g. add more fields or delete existing ones
3. Get Tags fields assigned to a table for a specific Tag Template

### Example

```
# Create an instance of the TagClient class
tag_client = TagClient(
    project_id="your-project-id",
    dataset_id="your-dataset-id",
    table_id="your-table-id",
    location="your-location",
    tag_template_id="your-tag-template-id"
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




