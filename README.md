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

#### pip
```code
pip install asposehtmlcloud
```

## Example

The examples below show how your application have to initiate and convert url to image using Aspose.HTML Cloud library:

```python
import os
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.rest import ApiException
from shutil import copy2

# Get keys from aspose site.
# There is free quota available. 
# For more details, see https://purchase.aspose.cloud/pricing

configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v3.0",
                              authPath="https://api.aspose.cloud/connect/token",
                              debug=True)
api = HtmlApi(configuration)

source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
try:

    # Convert url to image
    res = api.get_convert_document_to_image_by_url(
        source_url, out_format="jpeg", width=800, height=1000, left_margin=50, right_margin=100,
        top_margin=150, bottom_margin=200, resolution=300, folder="MY_REMOTE_FOLDER", storage=""
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

# Documentation for Html API Endpoints

All URIs are relative to *https://api.aspose.cloud/v3.0*

## ConversionApi 

- For conversion to images allowed formats is jpeg, png, bmp, tiff, gif. Input formats are html, epub, svg.

Method | HTTP request | Description
------------- | ------------- | -------------
**get_convert_document_to_image** | **GET** html/{name}/convert/image/{outFormat} | Convert the HTML document from the storage by its name to the specified image format.
**get_convert_document_to_image_by_url** | **GET** html/convert/image/{outFormat} | Convert the HTML page from the web by its URL to the specified image format.
**get_convert_document_to_pdf** | **GET** html/{name}/convert/pdf | Convert the HTML document from the storage by its name to PDF.
**get_convert_document_to_pdf_by_url** | **GET** html/convert/pdf | Convert the HTML page from the web by its URL to PDF.
**get_convert_document_to_xps** | **GET** html/{name}/convert/xps | Convert the HTML document from the storage by its name to XPS.
**get_convert_document_to_xps_by_url** | **GET** html/convert/xps | Convert the HTML page from the web by its URL to XPS.
**post_convert_document_in_request_to_image** | **POST** html/convert/image/{outFormat} | Converts the HTML document (in request content) to the specified image format and uploads resulting file to storage.
**post_convert_document_in_request_to_pdf** | **POST** html/convert/pdf | Converts the HTML document (in request content) to PDF and uploads resulting file to storage.
**post_convert_document_in_request_to_xps** | **POST** html/convert/xps | Converts the HTML document (in request content) to XPS and uploads resulting file to storage.
**put_convert_document_to_image** | **PUT** html/{name}/convert/image/{outFormat} | Converts the HTML document (located on storage) to the specified image format and uploads resulting file to storage.
**put_convert_document_to_pdf** | **PUT** html/{name}/convert/pdf | Converts the HTML document (located on storage) to PDF and uploads resulting file to storage.
**put_convert_document_to_xps** | **PUT** html/{name}/convert/xps | Converts the HTML document (located on storage) to XPS and uploads resulting file to storage.
**get_convert_document_to_mhtml_by_url** | **GET** /html/convert/mhtml | Converts the HTML page from Web by its URL to MHTML returns resulting file in response content.
**get_convert_document_to_markdown** | **GET** /html/{name}/convert/md | Converts the HTML document (located on storage) to Markdown and returns resulting file in response content.
**post_convert_document_in_request_to_markdown** | **POST** /html/convert/md | Converts the HTML document (in request content) to Markdown and uploads resulting file to storage by specified path.
**put_convert_document_to_markdown** | **PUT** /html/{name}/convert/md | Converts the HTML document (located on storage) to Markdown and uploads resulting file to storage by specified path.

## ImportApi

Method | HTTP request | Description
------------- | ------------- | -------------
**get_convert_markdown_to_html** | **GET** /html/{name}/convert/md | Converts the MarkdownHTML document (located on storage) to HTML and returns resulting file in response content.
**post_convert_markdown_in_request_to_html** | **POST** /html/import/md | Converts the MarkdownHTML document (in request content) to HTML and uploads resulting file to storage by specified path.
**put_convert_markdown_to_html** | **PUT** /html/{name}/import/md | Converts the Markdown document (located on storage) to HTML and uploads resulting file to storage by specified path.

## DocumentApi

Method | HTTP request | Description
------------- | ------------- | -------------
**get_document_by_url** | **GET** /html/download | Return all HTML page with linked resources packaged as a ZIP archive by the source page URL.
**get_document_fragment_by_x_path** | **GET** html/{name}/fragments/{outFormat} | Return list of HTML fragments matching the specified XPath query.
**get_document_fragment_by_x_path_by_url** | **GET** html/fragments/{outFormat} | Return list of HTML fragments matching the specified XPath query by the source page URL.
**get_document_fragments_by_css_selector** | **GET** /html/{name}/fragments/css/{outFormat} | Return list of HTML fragments matching the specified CSS selector.
**get_document_fragments_by_css_selector_by_url** | **GET** /html/fragments/css/{outFormat} | Return list of HTML fragments matching the specified CSS selector by the source page URL.
**get_document_images** | **GET** html/{name}/images/all | Return all HTML document images packaged as a ZIP archive.
**get_document_images_by_url** | **GET** html/images/all | Return all HTML page images packaged as a ZIP archive by the source page URL.

## SeoApi

Method | HTTP request | Description
------------- | ------------- | -------------
**get_seo_warning** | **GET** /html/seo | Page analysis and return SEO warnings in json format.
**get_html_warning** | **GET** /html/validator | Checks the markup validity of Web documents in HTML, XHTML, etc.and return in json format.

## TemplateMergeApi    

Method | HTTP request | Description
------------- | ------------- | -------------
**get_merge_html_template** | **GET** /html/{templateName}/merge | Populate HTML document template with data located as a file in the storage.
**post_merge_html_template** | **POST** /html/{templateName}/merge | Populate HTML document template with data from the request body. Result document will be saved to storage.

# Documentation for Storage API Endpoints

## StorageApi

Method | HTTP request | Description
------------- | ------------- | -------------
**copy_file** | **PUT** /html/storage/file/copy/{srcPath} | Copy file
**delete_file** | **DELETE** /html/storage/file/{path} | Delete file
**download_file** | **GET** /html/storage/file/{path} | Download file
**move_file** | **PUT** /html/storage/file/move/{srcPath} | Move file
**upload_file** | **PUT** /html/storage/file/{path} | Upload file
**copy_filder** | **PUT** /html/storage/folder/copy/{srcPath} | Copy folder
**create_folder** | **PUT** /html/storage/folder/{path} | Create the folder
**delete_folder** | **DELETE** /html/storage/folder/{path} | Delete folder
**get_files_list** | **GET** /html/storage/folder/{path} | Get all files and folders within a folder
**move_folder** | **PUT** /html/storage/folder/move/{srcPath} | Move folder
**get_disc_usage** | **GET** /html/storage/disc | Get disc usage
**get_file_versions** | **GET** /html/storage/version/{path} | Get file versions
**object_exists** | **GET** /html/storage/exist/{path} | Check if file or folder exists
**storage_exists** | **GET** /html/storage/{storageName}/exist | Check if storage exists


[Tests](https://github.com/aspose-html-cloud/aspose-html-cloud-python/tree/master/test) contain various examples of using the Aspose.HTML SDK.

[Docs](https://github.com/aspose-html-cloud/aspose-html-cloud-python/tree/master/docs/_build/html) Full documentation for Aspose.HTML SDK in html format.

## Dependencies
- [See requirements.txt](https://github.com/aspose-html-cloud/aspose-html-cloud-python/blob/master/requirements.txt)

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.aspose.cloud/html).
