# Aspose.HTML Cloud SDK for Python
This repository contains Aspose.HTML Cloud SDK for Python source code. This SDK allows you to work with Aspose.HTML Cloud REST APIs in your Python applications quickly and easily.

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

#### pip
```code
pip install asposehtmlcloud
```

## Example

The examples below show how your application have to initiate and convert url to image using Aspose.HTML Cloud library:

Possible conversions: 
- HTML -> PDF, XPS, DOCX, MD, MHTML, JPEG, BMP, PNG, TIFF, GIF
- EPUB -> PDF, XPS, DOCX, JPEG, BMP, PNG, TIFF, GIF
- MD -> PDF, XPS, DOCX, HTML, MHTML, JPEG, BMP, PNG, TIFF, GIF
- MHTML -> PDF, XPS, DOCX, JPEG, BMP, PNG, TIFF, GIF
- SVG -> PDF, XPS, JPEG, BMP, PNG, TIFF, GIF
- JPEG, BMP, PNG, TIFF, GIF -> SVG

```python
import os
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.rest import ApiException

# Get keys from aspose site.
# There is free quota available. 
# For more details, see https://purchase.aspose.cloud/pricing

configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v4.0",
                              authPath="https://api.aspose.cloud/connect/token",
                              debug=True)

client = Client(configuration)
html_api = HtmlApi(client)

source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
try:
    res = html_api.convert_url_to_local(input_file=source_url, output_file="result.pdf")
    if not os.path.exists(res.file):
        print('conversion failed')
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

# Documentation for Html API Endpoints

All URIs are relative to *https://api.aspose.cloud/v4.0*

## ConversionApi 

- See possible conversions.

| Method                                                               | Description                                             |
|----------------------------------------------------------------------|---------------------------------------------------------|
| **[vectorize_local_to_local](doc/VectorizeLocalToLocal.md)**         | Vectorize images from local disk to a local disk.       |
| **[vectorize_local_to_storage](doc/VectorizeLocalToStorage.md)**     | Vectorize images from local disk to user's storage.     |
| **[vectorize_storage_to_local](doc/VectorizeStorageToLocal.md)**     | Vectorize images from user's storage to local disk.     |
| **[vectorize_storage_to_storage](doc/VectorizeStorageToStorage.md)** | Vectorize images from user's storage to user's storage. |
| **[vectorize](doc/Vectorize.md)**                                    | Vectorize images to the svg format.                     |


## VectorizeApi 

- For vectorization images to svg format.

| Method                                                           | Description                                               |
|------------------------------------------------------------------|-----------------------------------------------------------|
| **[convert_local_to_local](doc/ConvertLocalToLocal.md)**         | Convert a document from local disk to a local disk.       |
| **[convert_local_to_storage](doc/ConvertLocalToStorage.md)**     | Convert a document from local disk to user's storage.     |
| **[convert_storage_to_local](doc/ConvertStorageToLocal.md)**     | Convert a document from user's storage to local disk.     |
| **[convert_storage_to_storage](doc/ConvertStorageToStorage.md)** | Convert a document from user's storage to user's storage. |
| **[convert_url_to_local](doc/ConvertUrlToLocal.md)**             | Convert the HTML document by URL to local disk.           |
| **[convert_url_to_storage](doc/ConvertUrlToStorage.md)**         | Convert the HTML document by URL to user's storage.       |
| **[convert](doc/Convert.md)**                                    | Convert a document to the specified format.               |

# Documentation for Storage API Endpoints

## StorageApi

| Method                                          | HTTP request                        | Description                               |
|-------------------------------------------------|-------------------------------------|-------------------------------------------|
| **[delete_file](doc/DeleteFile.md)**            | **DELETE** /html/file/              | Delete file                               |
| **[download_file](doc/DownloadFile.md)**        | **GET** /html/storage/file          | Download file                             |
| **[upload_file](doc/UploadFile.md)**            | **POST** /html/storage/file         | Upload file                               |
| **[create_folder](doc/CreateFolder.md)**        | **POST** /html/folder               | Create the folder                         |
| **[delete_folder](doc/DeleteFolder.md)**        | **DELETE** /html/folder             | Delete folder                             |
| **[get_files_list](doc/GetFilesList.md)**       | **GET** /html/folder                | Get all files and folders within a folder |
| **[get_disc_usage](doc/GetDiscUsage.md)**       | **GET** /html/storage/disc          | Get disc usage                            |
| **[object_exists](doc/ObjectExists.md)**        | **GET** /html/storage/exist         | Check if file or folder exists            |
| **[storage_exists](doc/StorageExists.md)**      | **GET** /html/storage/exist/storage | Check if storage exists                   |


[Tests](test/) contain various examples of using the Aspose.HTML SDK.

[Docs](html_doc/) Full documentation for Aspose.HTML SDK in html format.

## Dependencies
- [See requirements.txt](requirements.txt)

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.aspose.cloud/html).
