## delete_file

### Parameters
| Field             | Type | Description                              |
|-------------------|------|------------------------------------------|
| **path**          | str  | Full path to the file                    |
| **storage_name**  | str  | Storage name. Default is None (optional) |
| **version_id**    | str  | File version Id (optional)               |


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
    storage_api.delete_file("Folder_in_the_storage/file_for_delete.jpg");
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex
```
#### Return: Void
