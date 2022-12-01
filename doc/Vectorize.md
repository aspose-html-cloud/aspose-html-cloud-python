## vectorize

General vectorize function

Possible vectorization: 
- JPEG, BMP, PNG, TIFF, GIF -> SVG


### Parameters
| Parameter         | Type                                      | Description                                     |
|-------------------|-------------------------------------------|-------------------------------------------------|
| **input_file**    | str                                       | Full path to the image file                     |
| **output_file**   | str                                       | Full path to the output svg file with extension |
| **src_in_local**  | bool                                      | Source in the local disk                        |
| **dest_in_local** | bool                                      | Destination in the local disk                   |
| **options**       | [VectorizeOptions](VectorizeOptions.md)   | Vectorize options                               |
| **storage_name**  | str                                       | Storage name                                    |

### 

### Vectorize png file in the local disk to svg and save result to the local disk
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
    res = html_api.vectorize(input_file="c://test.png", output_file="c://test.svg", src_in_local=True,
                                      dest_in_local=True, options=None, storage_name=None)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Vectorize png image to svg with options and save result to the storage.
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
    res = html_api.vectorize(input_file=test.png, output_file="test.svg", src_in_local=False,
                                      dest_in_local=False, options=None, storage_name=None)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)