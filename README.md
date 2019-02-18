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

# Documentation for API Endpoints

All URIs are relative to *https://api.aspose.cloud/v1.1*

## ConversionApi

Method | HTTP request | Description
------------- | ------------- | -------------
**get_convert_document_to_image** | **GET** html/{name}/convert/image/{outFormat} | Convert the HTML document from the storage by its name to the specified image format.
**get_convert_document_to_image_by_url** | **GET** html/convert/image/{outFormat} | Convert the HTML page from the web by its URL to the specified image format.
**get_convert_document_to_pdf** | **GET** html/{name}/convert/pdf | Convert the HTML document from the storage by its name to PDF.
**get_convert_document_to_pdf_by_url** | **GET** html/convert/pdf | Convert the HTML page from the web by its URL to PDF.
**get_convert_document_to_xps** | **GET** html/{name}/convert/xps | Convert the HTML document from the storage by its name to XPS.
**get_convert_document_to_xps_by_url** | **GET** html/convert/xps | Convert the HTML page from the web by its URL to XPS.
**put_convert_document_in_request_to_image** | **PUT** html/convert/image/{outFormat} | Converts the HTML document (in request content) to the specified image format and uploads resulting file to storage.
**put_convert_document_in_request_to_pdf** | **PUT** html/convert/pdf | Converts the HTML document (in request content) to PDF and uploads resulting file to storage.
**put_convert_document_in_request_to_xps** | **PUT** html/convert/xps | Converts the HTML document (in request content) to XPS and uploads resulting file to storage.
**put_convert_document_to_image** | **PUT** html/{name}/convert/image/{outFormat} | Converts the HTML document (located on storage) to the specified image format and uploads resulting file to storage.
**put_convert_document_to_pdf** | **PUT** html/{name}/convert/pdf | Converts the HTML document (located on storage) to PDF and uploads resulting file to storage.
**put_convert_document_to_xps** | **PUT** html/{name}/convert/xps | Converts the HTML document (located on storage) to XPS and uploads resulting file to storage.
**get_convert_document_to_mhtml_by_url** | **GET** /html/convert/mhtml | Converts the HTML page from Web by its URL to MHTML returns resulting file in response content.
**get_convert_document_to_markdown** | **GET** /html/{name}/convert/md | Converts the HTML document (located on storage) to Markdown and returns resulting file in response content.
**put_convert_document_in_request_to_markdown** | **PUT** /html/convert/md | Converts the HTML document (in request content) to Markdown and uploads resulting file to storage by specified path.
**put_convert_document_to_markdown** | **PUT** /html/{name}/convert/md | Converts the HTML document (located on storage) to Markdown and uploads resulting file to storage by specified path.

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

## OcrApi

Method | HTTP request | Description
------------- | ------------- | -------------
**get_recognize_and_import_to_html** | **GET** html/{name}/ocr/import | Recognize text from the image file in the storage and import it to HTML format.
**get_recognize_and_translate_to_html** | **GET** html/{name}/ocr/translate/{srcLang}/{resLang} | Recognize text from the image file in the storage, import it to HTML format and translate to specified language.

## TranslationApi

Method | HTTP request | Description
------------- | ------------- | -------------
**get_translate_document** | **GET** html/{name}/translate/{srcLang}/{resLang} | Translate the HTML document specified by the name from default or specified storage. 
**get_translate_document_by_url** | **GET** html/translate/{srcLang}/{resLang} | Translate the HTML document from Web specified by its URL.

## SummarizationApi

Method | HTTP request | Description
------------- | ------------- | -------------
**get_detect_html_keywords** | **GET** html/{name}/summ/keywords | Get the HTML document keywords using the keyword detection service.
**get_detect_html_keywords_by_url** | **GET** html/summ/keywords | Get the keywords from HTML document from Web specified by its URL using the keyword detection service

## TemplateMergeApi    

Method | HTTP request | Description
------------- | ------------- | -------------
**get_merge_html_template** | **GET** /html/{templateName}/merge | Populate HTML document template with data located as a file in the storage.
**put_merge_html_template** | **PUT** /html/{templateName}/merge | Populate HTML document template with data from the request body. Result document will be saved to storage.


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
