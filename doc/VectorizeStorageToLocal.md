## vectorize_storage_to_local

Vectorize file in the storage to the local file.

Possible vectorization: 
- JPEG, BMP, PNG, TIFF, GIF -> SVG

### Parameters
| Parameter        | Type                                      | Description                                  |
|------------------|-------------------------------------------|----------------------------------------------|
| **input_file**   | str                                       | Full path in the storage to input image file |
| **output_file**  | str                                       | Full path to output svg file with extension  |
| **storage_name** | str                                       | User's storage name. None if default         |
| **options**      | [VectorizeOptions](VectorizeOptions.md)   | Vectorize options (optional)                 |

### 

### Vectorize png file in the storage to svg and save result to the local file
```python
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.rest import ApiException

configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v4.0",
                              authPath="https://api.aspose.cloud/connect/token",
                              debug=True)
client = Client(configuration)
html_api = HtmlApi(client)

try:
    res = html_api.vectorize_storage_to_local(input_file="test.png", output_file="test.svg", storage_name=None)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Vectorize png file in the storage to svg with options and save result to local file.
```python
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.rest import ApiException

configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v4.0",
                              authPath="https://api.aspose.cloud/connect/token",
                              debug=True)
client = Client(configuration)
html_api = HtmlApi(client)

options = {
	'error_threshold': 1,
	'max_iterations': 50,
	'colors_limit': 3,
	'line_width': 1,
}

try:
    res = html_api.vectorize_storage_to_local(input_file="test.png", output_file="test.svg",
                                                       storage_name=None, options=options)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)