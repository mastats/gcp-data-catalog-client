from google.oauth2 import service_account
from google.cloud import datacatalog_v1 as datacatalog

class TagClient:
    def __init__(self, project_id, dataset_id, table_id, location, tag_template_id, key_path):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.location = location
        self.tag_template_id = tag_template_id
        self.key_path = key_path
        
        self.credentials = self.get_credentials(key_path)
        self.datacatalog_client = self.create_datacatalog_client()
        self.table_entry = self.get_table_entry()
        self.tag_template_name = self.get_tag_template_name()
        self.tag = self.get_table_tag()
    
    def get_credentials(self, key_path):
        credentials = service_account.Credentials.from_service_account_file(
            key_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        return credentials
    
    def create_datacatalog_client(self):
        datacatalog_client = datacatalog.DataCatalogClient(
            credentials=self.credentials,
        )
        return datacatalog_client

    def get_table_entry(self):
        resource_name = (
            f"//bigquery.googleapis.com/projects/{self.project_id}/datasets/{self.dataset_id}/tables/{self.table_id}"
        )
        table_entry = self.datacatalog_client.lookup_entry(
            request={"linked_resource": resource_name}
        )
        return table_entry

    def get_tag_template_name(self):
        # Get an existing tag template
        tag_template_name = self.datacatalog_client.tag_template_path(
            self.project_id, self.location, self.tag_template_id
        )
        return tag_template_name
    
    def get_table_tag(self):
        # Get table tags
        table_tags = self.datacatalog_client.list_tags(parent=self.table_entry.name)
        for tag in table_tags:
            if tag.template == self.tag_template_name:
                return tag
        return False

    def get_field_type(self, field_name):
        # Retrieve the template fields & type
        tag_template = self.datacatalog_client.get_tag_template(name=self.tag_template_name)
        if field_name in tag_template.fields:
            field = tag_template.fields[field_name]
            return field.type_.primitive_type.name.lower() + '_value'
        else:
            raise KeyError(f'Field {field} not found in the tag template {tag_template}')

    def check_field_in_tag(self, field_name):
        # check if field is used in a tag assigned to a table
        if self.tag == False:
            return False # Tag not used in the present table
        else:
            if field_name in self.tag.fields:
                return True # the field and the tag are used
            else:
                return False # the tag is used but not the field

    def create_tag_instance(self, tags_dict):
        tag = datacatalog.types.Tag()
        tag.template = self.tag_template_name
        for field_name, value in tags_dict.items():
            if self.tag:
                raise KeyError('The tag is already assigned to the table')
            field_type = self.get_field_type(field_name)
            tag.fields[field_name] = datacatalog.types.TagField()
            setattr(tag.fields[field_name], field_type, value)
        tag = self.datacatalog_client.create_tag(parent=self.table_entry.name, tag=tag)
        return tag

    def update_tag_instance(self, tags_dict):
        if not self.tag:
            raise KeyError('The tag has not been created for this table')
        for field_name, value in tags_dict.items():
            field_type = self.get_field_type(field_name)
            if field_name not in self.tag.fields:
                self.tag.fields[field_name] = datacatalog.TagField()
            setattr(self.tag.fields[field_name], field_type, value)
        self.datacatalog_client.update_tag(tag=self.tag)
        return self.tag
