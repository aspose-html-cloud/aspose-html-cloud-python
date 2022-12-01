## vectorize_local_to_local

Vectorize an image that is placed in the local directory to the local svg file.

Possible vectorization: 
- JPEG, BMP, PNG, TIFF, GIF -> SVG

### Parameters
| Parameter        | Type                                      | Description                                 |
|------------------|-------------------------------------------|---------------------------------------------|
| **input_file**   | str                                       | Full path to input image for vectorization  |
| **output_file**  | str                                       | Full path to output svg file with extension |
| **options**      | [VectorizeOptions](VectorizeOptions.md)   | Vectorize options (optional)                |


### Vectorize jpeg file to svg
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
    res = html_api.vectorize_local_to_local(input_file="test.jpeg", output_file="test.svg")
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Vectorize local bmp file to svg with options and save result to the local svg file.
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
    res = html_api.vectorize_local_to_local(input_file="test.bmp", output_file="test.svg", options=options)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)