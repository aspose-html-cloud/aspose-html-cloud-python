# coding: utf-8
"""Copyright
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="html_api.py">
   Copyright (c) 2019 Aspose.HTML for Cloud
 </copyright>
 <summary>

  Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
</summary>
--------------------------------------------------------------------------------------------------------------------
"""

from __future__ import absolute_import

from asposehtmlcloud.alias import aliased
from asposehtmlcloud.alias import alias
from asposehtmlcloud.api_client import ApiClient

# python 2 and python 3 compatibility library
import six


@aliased
class HtmlApi(object):

    def __init__(self, config=None):
        if config is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(config)
        self.api_client = api_client

    ##########################################################
    #                  Conversion API
    ##########################################################

    @alias('getConvertDocumentToImage', 'GetConvertDocumentToImage')
    def get_convert_document_to_image(self, name, out_format, **kwargs):
        """Convert the HTML, EPUB, SVG documents from the storage by its name to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name (html, epub, svg formats). (required)
        :param str out_format: Resulting image format (jpeg, png, bmp, tiff, gif). (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int resolution: Resolution of resulting image.
        :param str folder: The source document folder.
        :param str storage: The source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_image_with_http_info(name, out_format, **kwargs)
        else:
            (data) = self.__get_convert_document_to_image_with_http_info(name, out_format, **kwargs)
            return data

    def __get_convert_document_to_image_with_http_info(self, name, out_format, **kwargs):
        """Convert the HTML, EPUB, SVG documents from the storage by its name to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name (html, epub, svg formats). (required)
        :param str out_format: Resulting image format (jpeg, png, bmp, tiff, gif). (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int resolution: Resolution of resulting image.
        :param str folder: The source document folder.
        :param str storage: The source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'out_format', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin', 'resolution', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_convert_document_to_image`")
        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `get_convert_document_to_image`")

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/image/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getConvertDocumentToImageByUrl', 'GetConvertDocumentToImageByUrl')
    def get_convert_document_to_image_by_url(self, source_url, out_format, **kwargs):
        """Convert the HTML page from the web by its URL to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str out_format: Resulting image format(jpeg, png, bmp, tiff, gif). (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int resolution: Resolution of resulting image.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_image_by_url_with_http_info(source_url, out_format, **kwargs)
        else:
            (data) = self.__get_convert_document_to_image_by_url_with_http_info(source_url, out_format, **kwargs)
            return data

    def __get_convert_document_to_image_by_url_with_http_info(self, source_url, out_format, **kwargs):
        """Convert the HTML page from the web by its URL to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str out_format: Resulting image format(jpeg, png, bmp, tiff, gif). (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int resolution: Resolution of resulting image.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'out_format', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin', 'resolution', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image_by_url" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError(
                "Missing the required parameter `source_url` when calling `get_convert_document_to_image_by_url`")

        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError(
                "Missing the required parameter `out_format` when calling `get_convert_document_to_image_by_url`")

        collection_formats = {}
        path_params = {}

        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/convert/image/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getConvertDocumentToPdf', 'GetConvertDocumentToPdf')
    def get_convert_document_to_pdf(self, name, **kwargs):
        """Convert the HTML, EPUB, SVG document from the storage by its name to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_pdf_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_convert_document_to_pdf_with_http_info(name, **kwargs)
            return data

    def __get_convert_document_to_pdf_with_http_info(self, name, **kwargs):
        """Convert the HTML, EPUB, SVG document from the storage by its name to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder',
                      'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_convert_document_to_pdf`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/pdf', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getConvertDocumentToPdfByUrl', 'GetConvertDocumentToPdfByUrl')
    def get_convert_document_to_pdf_by_url(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_pdf_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_convert_document_to_pdf_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_convert_document_to_pdf_by_url_with_http_info(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin',
                      'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_pdf_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError(
                "Missing the required parameter `source_url` when calling `get_convert_document_to_pdf_by_url`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/convert/pdf', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getConvertDocumentToXps', 'GetConvertDocumentToXps')
    def get_convert_document_to_xps(self, name, **kwargs):
        """Convert the HTML, EPUB, SVG document from the storage by its name to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_xps_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_convert_document_to_xps_with_http_info(name, **kwargs)
            return data

    def __get_convert_document_to_xps_with_http_info(self, name, **kwargs):
        """Convert the HTML, EPUB, SVG document from the storage by its name to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder',
                      'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_xps" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_convert_document_to_xps`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/xps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getConvertDocumentToXpsByUrl', 'GetConvertDocumentToXpsByUrl')
    def get_convert_document_to_xps_by_url(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_xps_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_convert_document_to_xps_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_convert_document_to_xps_by_url_with_http_info(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param int width: Resulting image width.
        :param int height: Resulting image height.
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin',
                      'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_xps_by_url" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError(
                "Missing the required parameter `source_url` when calling `get_convert_document_to_xps_by_url`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/convert/xps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('postConvertDocumentInRequestToImage', 'PostConvertDocumentInRequestToImage')
    def post_convert_document_in_request_to_image(self, out_path, out_format, file, **kwargs):
        """Converts the HTML, EPUB, SVG document (in request content) to the specified image format
        and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (jpeg, png, bmp, tiff, gif)(required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param int resolution: Resolution of resulting image. Default is 96 dpi.
        :return: File. If the method is called asynchronously,   returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_convert_document_in_request_to_image_with_http_info(out_path, out_format, file, **kwargs)
        else:
            (data) = self.__post_convert_document_in_request_to_image_with_http_info(out_path, out_format, file,
                                                                                     **kwargs)
            return data

    def __post_convert_document_in_request_to_image_with_http_info(self, out_path, out_format, file, **kwargs):
        """Converts the HTML, EPUB, SVG document (in request content) to the specified image format and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (jpeg, png, bmp, tiff, gif)(required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param int resolution: Resolution of resulting image. Default is 96 dpi.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['out_path', 'out_format', 'file', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin', 'resolution']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_document_in_request_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError(
                "Missing the required parameter `out_path` when calling `post_convert_document_in_request_to_image`")

        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError(
                "Missing the required parameter `out_format` when calling `post_convert_document_in_request_to_image`")

        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError(
                "Missing the required parameter `file` when calling `post_convert_document_in_request_to_image`")

        collection_formats = {}
        path_params = {}

        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        if 'file' in params:
            local_var_files['file'] = params['file']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api(
            '/html/convert/image/{outFormat}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('postConvertDocumentInRequestToPdf', 'PostConvertDocumentInRequestToPdf')
    def post_convert_document_in_request_to_pdf(self, out_path, file, **kwargs):
        """Converts the HTML, EPUB, SVG document (in request content) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.pdf) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_convert_document_in_request_to_pdf_with_http_info(out_path, file, **kwargs)
        else:
            (data) = self.__post_convert_document_in_request_to_pdf_with_http_info(out_path, file, **kwargs)
            return data

    def __post_convert_document_in_request_to_pdf_with_http_info(self, out_path, file, **kwargs):
        """Converts the HTML, EPUB, SVG document (in request content) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.pdf) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['out_path', 'file', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_document_in_request_to_pdf" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError(
                "Missing the required parameter `out_path` when calling `post_convert_document_in_request_to_pdf`")

        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError(
                "Missing the required parameter `file` when calling `post_convert_document_in_request_to_pdf`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        if 'file' in params:
            local_var_files['file'] = params['file']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api(
            '/html/convert/pdf', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('postConvertDocumentInRequestToXps', 'PostConvertDocumentInRequestToXps')
    def post_convert_document_in_request_to_xps(self, out_path, file, **kwargs):
        """Converts the HTML, EPUB, SVG document (in request content) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.xps) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_convert_document_in_request_to_xps_with_http_info(out_path, file, **kwargs)
        else:
            (data) = self.__post_convert_document_in_request_to_xps_with_http_info(out_path, file, **kwargs)
            return data

    def __post_convert_document_in_request_to_xps_with_http_info(self, out_path, file, **kwargs):
        """Converts the HTML, EPUB, SVG document (in request content) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.xps) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['out_path', 'file', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_document_in_request_to_xps" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError(
                "Missing the required parameter `out_path` when calling `post_convert_document_in_request_to_xps`")

        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError(
                "Missing the required parameter `file` when calling `post_convert_document_in_request_to_xps`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        if 'file' in params:
            local_var_files['file'] = params['file']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api(
            '/html/convert/xps', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('putConvertDocumentToImage', 'PutConvertDocumentToImage')
    def put_convert_document_to_image(self, name, out_path, out_format, **kwargs):
        """Converts the HTML, EPUB, SVG document (located on storage) to the specified image format and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (jpeg, png, bmp, tiff, gif)(required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param int resolution: Resolution of resulting image. Default is 96 dpi.
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__put_convert_document_to_image_with_http_info(name, out_path, out_format, **kwargs)
        else:
            (data) = self.__put_convert_document_to_image_with_http_info(name, out_path, out_format, **kwargs)
            return data

    def __put_convert_document_to_image_with_http_info(self, name, out_path, out_format, **kwargs):
        """Converts the HTML, EPUB, SVG document (located on storage) to the specified image format and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (jpeg, png, bmp, tiff, gif)(required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param int resolution: Resolution of resulting image. Default is 96 dpi.
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'out_path', 'out_format', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin', 'resolution', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `put_convert_document_to_image`")

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` when calling `put_convert_document_to_image`")

        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `put_convert_document_to_image`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']
        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/image/{outFormat}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('putConvertDocumentToPdf', 'PutConvertDocumentToPdf')
    def put_convert_document_to_pdf(self, name, out_path, **kwargs):
        """Converts the HTML, EPUB, SVG document (located on storage) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.pdf) (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__put_convert_document_to_pdf_with_http_info(name, out_path, **kwargs)
        else:
            (data) = self.__put_convert_document_to_pdf_with_http_info(name, out_path, **kwargs)
            return data

    def __put_convert_document_to_pdf_with_http_info(self, name, out_path, **kwargs):
        """Converts the HTML, EPUB, SVG document (located on storage) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.pdf) (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'out_path', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document_to_pdf" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `put_convert_document_to_pdf`")

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` when calling `put_convert_document_to_pdf`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/pdf', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('putConvertDocumentToXps', 'PutConvertDocumentToXps')
    def put_convert_document_to_xps(self, name, out_path, **kwargs):
        """Converts the HTML, EPUB, SVG document (located on storage) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.xps) (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__put_convert_document_to_xps_with_http_info(name, out_path, **kwargs)
        else:
            (data) = self.__put_convert_document_to_xps_with_http_info(name, out_path, **kwargs)
            return data

    def __put_convert_document_to_xps_with_http_info(self, name, out_path, **kwargs):
        """Converts the HTML, EPUB, SVG document (located on storage) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.xps) (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'out_path', 'width', 'height', 'left_margin', 'right_margin', 'top_margin',
                      'bottom_margin', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document_to_xps" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `put_convert_document_to_xps`")

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` when calling `put_convert_document_to_xps`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'left_margin' in params:
            query_params.append(('leftMargin', params['left_margin']))
        if 'right_margin' in params:
            query_params.append(('rightMargin', params['right_margin']))
        if 'top_margin' in params:
            query_params.append(('topMargin', params['top_margin']))
        if 'bottom_margin' in params:
            query_params.append(('bottomMargin', params['bottom_margin']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/xps', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getConvertDocumentToMhtmlByUrl', 'GetConvertDocumentToMhtmlByUrl')
    def get_convert_document_to_mhtml_by_url(self, source_url, **kwargs):
        """Converts the HTML page from Web by its URL to MHTML returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_mhtml_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_convert_document_to_mhtml_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_convert_document_to_mhtml_by_url_with_http_info(self, source_url, **kwargs):
        """Converts the HTML page from Web by its URL to MHTML returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param async_req bool
        :param str source_url: Source page URL. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_url']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversion_get_convert_document_to_mhtml_by_url" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError(
                "Missing the required parameter `source_url` when calling `get_convert_document_to_mhtml_by_url`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/convert/mhtml', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getConvertDocumentToMarkdown', 'GetConvertDocumentToMarkdown')
    def get_convert_document_to_markdown(self, name, **kwargs):
        """Converts the HTML document (located on storage) to Markdown and returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :param str folder: Source document folder.
        :param str storage: Source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_document_to_markdown_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_convert_document_to_markdown_with_http_info(name, **kwargs)
            return data

    def __get_convert_document_to_markdown_with_http_info(self, name, **kwargs):
        """Converts the HTML document (located on storage) to Markdown and returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :param str folder: Source document folder.
        :param str storage: Source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'use_git', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_markdown" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_convert_document_to_markdown`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'use_git' in params:
            query_params.append(('useGit', params['use_git']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/md', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('postConvertDocumentInRequestToMarkdown', 'PostConvertDocumentInRequestToMarkdown')
    def post_convert_document_in_request_to_markdown(self, out_path, file, **kwargs):
        """Converts the HTML document (in request content) to Markdown and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.md) (required)
        :param file file: A file to be converted. (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_convert_document_in_request_to_markdown_with_http_info(out_path, file, **kwargs)
        else:
            (data) = self.__post_convert_document_in_request_to_markdown_with_http_info(out_path, file, **kwargs)
            return data

    def __post_convert_document_in_request_to_markdown_with_http_info(self, out_path, file, **kwargs):
        """Converts the HTML document (in request content) to Markdown and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.md) (required)
        :param file file: A file to be converted. (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['out_path', 'file', 'use_git']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_document_in_request_to_markdown" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError(
                "Missing the required parameter `out_path` when calling `post_convert_document_in_request_to_markdown`")

        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError(
                "Missing the required parameter `file` when calling `post_convert_document_in_request_to_markdown`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'use_git' in params:
            query_params.append(('useGit', params['use_git']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        if 'file' in params:
            local_var_files['file'] = params['file']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api(
            '/html/convert/md', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('putConvertDocumentToMarkdown', 'PutConvertDocumentToMarkdown')
    def put_convert_document_to_markdown(self, name, out_path, **kwargs):
        """Converts the HTML document (located on storage) to Markdown and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.md) (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__put_convert_document_to_markdown_with_http_info(name, out_path, **kwargs)
        else:
            (data) = self.__put_convert_document_to_markdown_with_http_info(name, out_path, **kwargs)
            return data

    def __put_convert_document_to_markdown_with_http_info(self, name, out_path, **kwargs):
        """Converts the HTML document (located on storage) to Markdown and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.md) (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'out_path', 'use_git', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document_to_markdown" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `put_convert_document_to_markdown`")

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError(
                "Missing the required parameter `out_path` when calling `put_convert_document_to_markdown`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'use_git' in params:
            query_params.append(('useGit', params['use_git']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/convert/md', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    ##########################################################
    #                 Import API
    ##########################################################

    @alias('getConvertMarkdownToHtml', 'GetConvertMarkdownToHtml')
    def get_convert_markdown_to_html(self, name, **kwargs):
        """Converts the Markdown document (located on storage) to HTML and
        returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str folder: Source document folder.
        :param str storage: Source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_convert_markdown_to_html_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_convert_markdown_to_html_with_http_info(name, **kwargs)
            return data

    def __get_convert_markdown_to_html_with_http_info(self, name, **kwargs):
        """Converts the Markdown document (located on storage) to HTML
        and returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str folder: Source document folder.
        :param str storage: Source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_markdown_to_html" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_convert_markdown_to_html`")

        collection_formats = {}
        path_params = {'name': params['name']}

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/import/md', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('postConvertMarkdownInRequestToHtml', 'PostConvertMarkdownInRequestToHtml')
    def post_convert_markdown_in_request_to_html(self, out_path, file, **kwargs):
        """Converts the Markdown document (in request content) to HTML
        and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.html) (required)
        :param file file: A file to be converted. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_convert_markdown_in_request_to_html_with_http_info(out_path, file, **kwargs)
        else:
            (data) = self.__post_convert_markdown_in_request_to_html_with_http_info(out_path, file, **kwargs)
            return data

    def __post_convert_markdown_in_request_to_html_with_http_info(self, out_path, file, **kwargs):
        """Converts the Markdown document (in request content) to HTML
        and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.html) (required)
        :param file file: A file to be converted. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['out_path', 'file']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_convert_markdown_in_request_to_html" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` "
                             "when calling `post_convert_markdown_in_request_"
                             "to_html`")

        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` "
                             "when calling `post_convert_markdown_in_"
                             "request_to_html`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))

        header_params = {}
        form_params = []
        local_var_files = {'file': params['file']}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api(
            '/html/import/md', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('putConvertMarkdownToHtml', 'PutConvertMarkdownToHtml')
    def put_convert_markdown_to_html(self, name, out_path, **kwargs):
        """Converts the Markdown document (located on storage) to HTML
        and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.html) (required)
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__put_convert_markdown_to_html_with_http_info(name, out_path, **kwargs)
        else:
            (data) = self.__put_convert_markdown_to_html_with_http_info(name, out_path, **kwargs)
            return data

    def __put_convert_markdown_to_html_with_http_info(self, name, out_path, **kwargs):
        """Converts the Markdown document (located on storage) to HTML
        and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.html) (required)
        :param str folder: The source document folder.
        :param str storage: The source and resulting document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'out_path', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_markdown_to_html" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required "
                             "parameter `name` when calling "
                             "`put_convert_markdown_to_html`")

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` "
                             "when calling `put_convert_markdown_to_html`")

        collection_formats = {}
        path_params = {'name': params['name']}

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/import/md', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    ##########################################################
    #                 Document API
    ##########################################################

    @alias('getDocumentByUrl', 'GetDocumentByUrl')
    def get_document_by_url(self, source_url, **kwargs):
        """Return all HTML page with linked resources packaged as a ZIP archive by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_document_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_document_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_document_by_url_with_http_info(self, source_url, **kwargs):
        """Return all HTML page with linked resources packaged as a ZIP archive by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_by_url" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `get_document_by_url`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getDocumentFragmentByXPath', 'GetDocumentFragmentByXPath')
    def get_document_fragment_by_x_path(self, name, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: The document name (required). Presented as zip archive with one html file in the root or html file.
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :param str storage: The document storage.
        :param str folder: The document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_document_fragment_by_x_path_with_http_info(name, x_path, out_format, **kwargs)
        else:
            (data) = self.__get_document_fragment_by_x_path_with_http_info(name, x_path, out_format, **kwargs)
            return data

    def __get_document_fragment_by_x_path_with_http_info(self, name, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: The document name (required). Presented as zip archive with one html file in the root or html file.
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :param str storage: The document storage.
        :param str folder: The document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'x_path', 'out_format', 'storage', 'folder']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_fragment_by_x_path" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_document_fragment_by_x_path`")

        # verify the required parameter 'x_path' is set
        if ('x_path' not in params or
                params['x_path'] is None):
            raise ValueError("Missing the required parameter `x_path` when calling `get_document_fragment_by_x_path`")

        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError(
                "Missing the required parameter `out_format` when calling `get_document_fragment_by_x_path`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']
        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'x_path' in params:
            query_params.append(('xPath', params['x_path']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/fragments/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getDocumentFragmentByXPathByUrl', 'GetDocumentFragmentByXPathByUrl')
    def get_document_fragment_by_x_path_by_url(self, source_url, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_document_fragment_by_x_path_by_url_with_http_info(source_url, x_path, out_format,
                                                                                **kwargs)
        else:
            (data) = self.__get_document_fragment_by_x_path_by_url_with_http_info(source_url, x_path, out_format,
                                                                                  **kwargs)
            return data

    def __get_document_fragment_by_x_path_by_url_with_http_info(self, source_url, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'x_path', 'out_format']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_fragment_by_x_path_by_url" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError(
                "Missing the required parameter `source_url` when calling `get_document_fragment_by_x_path_by_url`")

        # verify the required parameter 'x_path' is set
        if ('x_path' not in params or
                params['x_path'] is None):
            raise ValueError(
                "Missing the required parameter `x_path` when calling `get_document_fragment_by_x_path_by_url`")

        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError(
                "Missing the required parameter `out_format` when calling `get_document_fragment_by_x_path_by_url`")

        collection_formats = {}
        path_params = {}

        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))
        if 'x_path' in params:
            query_params.append(('xPath', params['x_path']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/fragments/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getDocumentFragmentByCssSelector', 'GetDocumentFragmentByCssSelector')
    def get_document_fragments_by_css_selector(self, name, selector, out_format, **kwargs):
        """Return list of HTML fragments matching the specified CSS selector.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: The document name (required). Presented as zip archive with one html file in the root or html file.
        :param str selector: CSS selector string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_document_fragments_by_css_selector_with_http_info(name, selector, out_format, **kwargs)
        else:
            (data) = self.__get_document_fragments_by_css_selector_with_http_info(name, selector, out_format, **kwargs)
            return data

    def __get_document_fragments_by_css_selector_with_http_info(self, name, selector, out_format, **kwargs):
        """Return list of HTML fragments matching the specified CSS selector.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: The document name (required). Presented as zip archive with one html file in the root or html file.
        :param str selector: CSS selector string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'selector', 'out_format', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_fragments_by_css_selector" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError(
                "Missing the required parameter `name` when calling `get_document_fragments_by_css_selector`")

        # verify the required parameter 'selector' is set
        if ('selector' not in params or
                params['selector'] is None):
            raise ValueError(
                "Missing the required parameter `selector` when calling `get_document_fragments_by_css_selector`")

        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError(
                "Missing the required parameter `out_format` when calling `get_document_fragments_by_css_selector`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'selector' in params:
            query_params.append(('selector', params['selector']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/fragments/css/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getDocumentFragmentByCssSelectorByUrl', 'GetDocumentFragmentByCssSelectorByUrl')
    def get_document_fragments_by_css_selector_by_url(self, source_url, selector, out_format, **kwargs):
        """Return list of HTML fragments matching the specified CSS selector by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str selector: CSS selector string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_document_fragments_by_css_selector_by_url_with_http_info(source_url, selector, out_format,
                                                                                       **kwargs)
        else:
            (data) = self.__get_document_fragments_by_css_selector_by_url_with_http_info(source_url, selector,
                                                                                         out_format, **kwargs)
            return data

    def __get_document_fragments_by_css_selector_by_url_with_http_info(self, source_url, selector, out_format,
                                                                       **kwargs):
        """Return list of HTML fragments matching the specified CSS selector by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str selector: CSS selector string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'selector', 'out_format']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_fragments_by_css_selector_by_url" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError(
                "Missing the required parameter `source_url` when calling `get_document_fragments_by_css_selector_by_url`")

        # verify the required parameter 'selector' is set
        if ('selector' not in params or
                params['selector'] is None):
            raise ValueError(
                "Missing the required parameter `selector` when calling `get_document_fragments_by_css_selector_by_url`")

        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError(
                "Missing the required parameter `out_format` when calling `get_document_fragments_by_css_selector_by_url`")

        collection_formats = {}
        path_params = {}

        if 'out_format' in params:
            path_params['outFormat'] = params['out_format']

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))
        if 'selector' in params:
            query_params.append(('selector', params['selector']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/fragments/css/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getDocumentImages', 'GetDocumentImages')
    def get_document_images(self, name, **kwargs):
        """Return all HTML document images packaged as a ZIP archive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: The document name (required). Presented as zip archive with one html file in the root.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_document_images_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_document_images_with_http_info(name, **kwargs)
            return data

    def __get_document_images_with_http_info(self, name, **kwargs):
        """Return all HTML document images packaged as a ZIP archive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: The document name (required). Presented as zip archive with one html file in the root.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_images" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_document_images`")

        collection_formats = {}
        path_params = {}

        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{name}/images/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('getDocumentImagesByUrl', 'GetDocumentImagesByUrl')
    def get_document_images_by_url(self, source_url, **kwargs):
        """Return all HTML page images packaged as a ZIP archive by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_document_images_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_document_images_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_document_images_by_url_with_http_info(self, source_url, **kwargs):
        """Return all HTML page images packaged as a ZIP archive by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_images_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `get_document_images_by_url`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'source_url' in params:
            query_params.append(('sourceUrl', params['source_url']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/images/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    ##########################################################
    #                  TemplateMerge API
    ##########################################################

    @alias('getMergeHtmlTemplate', 'GetMergeHtmlTemplate')
    def get_merge_html_template(self, template_name, data_path, **kwargs):
        """Populate HTML document template with data located as a file in the storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str template_name: Template document name. Template document is HTML or zipped HTML. (required)
        :param str data_path: Data source file path in the storage. Supported data format: XML (required)
        :param str options: Template merge options: reserved for further implementation.
        :param str folder: The template document folder.
        :param str storage: The template document and data source storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_merge_html_template_with_http_info(template_name, data_path, **kwargs)
        else:
            (data) = self.__get_merge_html_template_with_http_info(template_name, data_path, **kwargs)
            return data

    def __get_merge_html_template_with_http_info(self, template_name, data_path, **kwargs):
        """Populate HTML document template with data located as a file in the storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str template_name: Template document name. Template document is HTML or zipped HTML. (required)
        :param str data_path: Data source file path in the storage. Supported data format: XML (required)
        :param str options: Template merge options: reserved for further implementation.
        :param str folder: The template document folder.
        :param str storage: The template document and data source storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['template_name', 'data_path', 'options', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_merge_html_template" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'template_name' is set
        if ('template_name' not in params or
                params['template_name'] is None):
            raise ValueError("Missing the required parameter `template_name` when calling `get_merge_html_template`")

        # verify the required parameter 'data_path' is set
        if ('data_path' not in params or
                params['data_path'] is None):
            raise ValueError("Missing the required parameter `data_path` when calling `get_merge_html_template`")

        collection_formats = {}

        path_params = {}
        if 'template_name' in params:
            path_params['templateName'] = params['template_name']

        query_params = []
        if 'data_path' in params:
            query_params.append(('dataPath', params['data_path']))
        if 'options' in params:
            query_params.append(('options', params['options']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/{templateName}/merge', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @alias('postMergeHtmlTemplate', 'PostMergeHtmlTemplate')
    def post_merge_html_template(self, template_name, out_path, file, **kwargs):
        """Populate HTML document template with data from the request body. Result document will be saved to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str template_name: Template document name. Template document is HTML or zipped HTML. (required)
        :param str out_path: Result document path. (required)
        :param file file: A data file to populate template. (required)
        :param str options: Template merge options: reserved for further implementation.
        :param str folder: The template document folder.
        :param str storage: The template document and data source storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_merge_html_template_with_http_info(template_name, out_path, file, **kwargs)
        else:
            (data) = self.__post_merge_html_template_with_http_info(template_name, out_path, file, **kwargs)
            return data

    def __post_merge_html_template_with_http_info(self, template_name, out_path, file, **kwargs):
        """Populate HTML document template with data from the request body. Result document will be saved to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str template_name: Template document name. Template document is HTML or zipped HTML. (required)
        :param str out_path: Result document path. (required)
        :param file file: A data file to populate template. (required)
        :param str options: Template merge options: reserved for further implementation.
        :param str folder: The template document folder.
        :param str storage: The template document and data source storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['template_name', 'out_path', 'file', 'options', 'folder', 'storage']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_merge_html_template" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'template_name' is set
        if ('template_name' not in params or
                params['template_name'] is None):
            raise ValueError("Missing the required parameter `template_name` when calling `post_merge_html_template`")

        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` when calling `post_merge_html_template`")

        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `post_merge_html_template`")

        collection_formats = {}
        path_params = {}

        if 'template_name' in params:
            path_params['templateName'] = params['template_name']

        query_params = []
        if 'out_path' in params:
            query_params.append(('outPath', params['out_path']))
        if 'options' in params:
            query_params.append(('options', params['options']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        if 'file' in params:
            local_var_files['file'] = params['file']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api(
            '/html/{templateName}/merge', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
