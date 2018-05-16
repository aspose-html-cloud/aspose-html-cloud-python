# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="conversion_api.py">
   Copyright (c) 2018 Aspose.HTML for Cloud
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

from asposehtmlcloud.api_client import ApiClient


# python 2 and python 3 compatibility library
import six


class ConversionApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def conversion_get_convert_document_to_image(self, name, out_format, **kwargs):
        """Convert the HTML document from the storage by its name to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str out_format: Resulting image format. (required)
        :param int width: Resulting image width. 
        :param int height: Resulting image height. 
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int x_resolution: Horizontal resolution of resulting image.
        :param int y_resolution: Vertical resolution of resulting image.
        :param str folder: The source document folder.
        :param str storage: The source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__conversion_get_convert_document_to_image_with_http_info(name, out_format, **kwargs)
        else:
            (data) = self.__conversion_get_convert_document_to_image_with_http_info(name, out_format, **kwargs)
            return data

    def __conversion_get_convert_document_to_image_with_http_info(self, name, out_format, **kwargs):
        """Convert the HTML document from the storage by its name to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str out_format: Resulting image format. (required)
        :param int width: Resulting image width. 
        :param int height: Resulting image height. 
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int x_resolution: Horizontal resolution of resulting image.
        :param int y_resolution: Vertical resolution of resulting image.
        :param str folder: The source document folder.
        :param str storage: The source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'out_format', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'x_resolution', 'y_resolution', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversion_get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `conversion_get_convert_document_to_image`")
        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `conversion_get_convert_document_to_image`")

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
        if 'x_resolution' in params:
            query_params.append(('xResolution', params['x_resolution']))
        if 'y_resolution' in params:
            query_params.append(('yResolution', params['y_resolution']))
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/convert/image/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def conversion_get_convert_document_to_image_by_url(self, source_url, out_format, **kwargs):
        """Convert the HTML page from the web by its URL to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str out_format: Resulting image format. (required)
        :param int width: Resulting image width. 
        :param int height: Resulting image height. 
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int x_resolution: Horizontal resolution of resulting image.
        :param int y_resolution: Vertical resolution of resulting image.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__conversion_get_convert_document_to_image_by_url_with_http_info(source_url, out_format, **kwargs)
        else:
            (data) = self.__conversion_get_convert_document_to_image_by_url_with_http_info(source_url, out_format, **kwargs)
            return data

    def __conversion_get_convert_document_to_image_by_url_with_http_info(self, source_url, out_format, **kwargs):
        """Convert the HTML page from the web by its URL to the specified image format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str out_format: Resulting image format. (required)
        :param int width: Resulting image width. 
        :param int height: Resulting image height. 
        :param int left_margin: Left resulting image margin.
        :param int right_margin: Right resulting image margin.
        :param int top_margin: Top resulting image margin.
        :param int bottom_margin: Bottom resulting image margin.
        :param int x_resolution: Horizontal resolution of resulting image.
        :param int y_resolution: Vertical resolution of resulting image.
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'out_format', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'x_resolution', 'y_resolution', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversion_get_convert_document_to_image_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `conversion_get_convert_document_to_image_by_url`")
        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `conversion_get_convert_document_to_image_by_url`")

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
        if 'x_resolution' in params:
            query_params.append(('xResolution', params['x_resolution']))
        if 'y_resolution' in params:
            query_params.append(('yResolution', params['y_resolution']))
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/convert/image/{outFormat}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def conversion_get_convert_document_to_pdf(self, name, **kwargs):
        """Convert the HTML document from the storage by its name to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__conversion_get_convert_document_to_pdf_with_http_info(name, **kwargs)
        else:
            (data) = self.__conversion_get_convert_document_to_pdf_with_http_info(name, **kwargs)
            return data

    def __conversion_get_convert_document_to_pdf_with_http_info(self, name, **kwargs):
        """Convert the HTML document from the storage by its name to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['name', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversion_get_convert_document_to_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `conversion_get_convert_document_to_pdf`")

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/convert/pdf', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def conversion_get_convert_document_to_pdf_by_url(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__conversion_get_convert_document_to_pdf_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__conversion_get_convert_document_to_pdf_by_url_with_http_info(source_url, **kwargs)
            return data

    def __conversion_get_convert_document_to_pdf_by_url_with_http_info(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to PDF.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['source_url', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversion_get_convert_document_to_pdf_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `conversion_get_convert_document_to_pdf_by_url`")

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/convert/pdf', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def conversion_get_convert_document_to_xps(self, name, **kwargs):
        """Convert the HTML document from the storage by its name to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__conversion_get_convert_document_to_xps_with_http_info(name, **kwargs)
        else:
            (data) = self.__conversion_get_convert_document_to_xps_with_http_info(name, **kwargs)
            return data

    def __conversion_get_convert_document_to_xps_with_http_info(self, name, **kwargs):
        """Convert the HTML document from the storage by its name to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['name', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversion_get_convert_document_to_xps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `conversion_get_convert_document_to_xps`")

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/convert/xps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def conversion_get_convert_document_to_xps_by_url(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__conversion_get_convert_document_to_xps_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__conversion_get_convert_document_to_xps_by_url_with_http_info(source_url, **kwargs)
            return data

    def __conversion_get_convert_document_to_xps_by_url_with_http_info(self, source_url, **kwargs):
        """Convert the HTML page from the web by its URL to XPS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['source_url', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversion_get_convert_document_to_xps_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `conversion_get_convert_document_to_xps_by_url`")

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/convert/xps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
