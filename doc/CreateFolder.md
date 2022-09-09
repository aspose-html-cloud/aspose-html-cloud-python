## create_folder

### Parameters
| Field             | Type | Description              |
|-------------------|------|--------------------------|
| **path**          | str  | Full path to the folder  |
| **storage_name**  | str  | Storage name (optional)  |



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
    storage_api.create_folder("Folder_in_the_storage/Subfolder");
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex
```
#### Return: Void
