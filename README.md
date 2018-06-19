# Aspose.HTML Cloud SDK for Python
This repository contains Aspose.HTML Cloud SDK for Python source code. This SDK allows you to work with Aspose.HTML Cloud REST APIs in your Python applications quickly and easily.

See [API Reference](https://apireference.aspose.cloud/html/) for full API specification.
## How to use the SDK?
The complete source code is available in this repository folder, you can either directly use it in your project via pip package manager.

### Prerequisites

To use Aspose HTML for Cloud Python SDK you need to register an account with [Aspose Cloud](https://www.aspose.cloud/) and lookup/create App Key and SID at [Cloud Dashboard](https://dashboard.aspose.cloud/#/apps). There is free quota available. For more details, see [Aspose Cloud Pricing](https://purchase.aspose.cloud/pricing).

### Installation

#### Install Aspose.HTML Cloud 

From the command line:
```code
	python setup.py install
```

#### From maven
```code
pip install asposehtmlcloud
```


The examples below show how your application have to initiate and convert url to image using Aspose.HTML Cloud library:
```python
import os
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.rest import ApiException
from shutil import copy2
configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v1.1",
                              authPath="https://api.aspose.cloud/oauth2/token",
                              debug=True)
api = HtmlApi(configuration)

source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
try:

    # Convert url to image
    res = api.get_convert_document_to_image_by_url(
        source_url, out_format="jpeg", width=800, height=1000, left_margin=50, right_margin=100,
        top_margin=150, bottom_margin=200, x_resolution=300, y_resolution=300,
        folder="MY_REMOTE_FOLDER", storage=""
    )

    src = str(res)
    # Move to test folder
    if os.path.isfile(src):
        copy2(src, '/home/user/testfolder/')
        os.remove(src)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

# ...
```

[Tests](./test/) contain various examples of using the Aspose.HTML SDK.

[Docs](./docs/html/_build/html/) Full documentation for Aspose.HTML Api SDK


Aspose HTML includes Aspose.Storage.Cloud to manipulate files on a remote server. This is used in tests for download test files to the server.

[Tests](./teststorageapi/) contain various examples of using the Aspose.Storage SDK.

[Docs](./docs/storage/_build/html/)  Full documentation for Aspose.Storage Api SDK


## Dependencies
- [See requirements.txt](./requirements.txt)


## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.aspose.cloud/html).
