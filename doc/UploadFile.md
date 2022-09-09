## upload_file

| Field            | Type | Description                              |
|------------------|------|------------------------------------------|
| **path**         | str  | Directory in the storage                 |
| **file**         | str  | Full path to the file                    |
| **storage_name** | str  | Storage name. Default is None (optional) |


```python
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.storage_api import StorageApi
from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.rest import ApiException

configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v4.0",
                              authPath="https://api.aspose.cloud/connect/token",
                              debug=True)
client = Client(configuration)
storage_api = StorageApi(client)

try:
    res = storage_api.upload_file("Folder_in_the_storage", "c://file_for_upload.jpg");
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex
```

#### Return: [FilesUploadResult](FileUploadResult.md)