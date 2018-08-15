# coding: utf-8
"""Copyright
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="html_api.py">
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

    def get_convert_document_to_image(self, name, out_format, **kwargs):
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
            return self.__get_convert_document_to_image_with_http_info(name, out_format, **kwargs)
        else:
            (data) = self.__get_convert_document_to_image_with_http_info(name, out_format, **kwargs)
            return data

    def __get_convert_document_to_image_with_http_info(self, name, out_format, **kwargs):
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

    def get_convert_document_to_image_by_url(self, source_url, out_format, **kwargs):
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
            return self.__get_convert_document_to_image_by_url_with_http_info(source_url, out_format, **kwargs)
        else:
            (data) = self.__get_convert_document_to_image_by_url_with_http_info(source_url, out_format, **kwargs)
            return data

    def __get_convert_document_to_image_by_url_with_http_info(self, source_url, out_format, **kwargs):
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
                    " to method get_convert_document_to_image_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `get_convert_document_to_image_by_url`")
        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `get_convert_document_to_image_by_url`")

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

    def get_convert_document_to_pdf(self, name, **kwargs):
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
            return self.__get_convert_document_to_pdf_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_convert_document_to_pdf_with_http_info(name, **kwargs)
            return data

    def __get_convert_document_to_pdf_with_http_info(self, name, **kwargs):
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

    def get_convert_document_to_pdf_by_url(self, source_url, **kwargs):
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
            return self.__get_convert_document_to_pdf_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_convert_document_to_pdf_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_convert_document_to_pdf_by_url_with_http_info(self, source_url, **kwargs):
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
                    " to method get_convert_document_to_pdf_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `get_convert_document_to_pdf_by_url`")

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

    def get_convert_document_to_xps(self, name, **kwargs):
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
            return self.__get_convert_document_to_xps_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_convert_document_to_xps_with_http_info(name, **kwargs)
            return data

    def __get_convert_document_to_xps_with_http_info(self, name, **kwargs):
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

    def get_convert_document_to_xps_by_url(self, source_url, **kwargs):
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
            return self.__get_convert_document_to_xps_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_convert_document_to_xps_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_convert_document_to_xps_by_url_with_http_info(self, source_url, **kwargs):
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
                    " to method get_convert_document_to_xps_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `get_convert_document_to_xps_by_url`")

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

    def put_convert_document_in_request_to_image(self, out_path, out_format, file, **kwargs):
        """Converts the HTML document (in request content) to the specified image format and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (required)
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
        if kwargs.get('async'):
            return self.__put_convert_document_in_request_to_image_with_http_info(out_path, out_format, file, **kwargs)
        else:
            (data) = self.__put_convert_document_in_request_to_image_with_http_info(out_path, out_format, file, **kwargs)
            return data

    def __put_convert_document_in_request_to_image_with_http_info(self, out_path, out_format, file, **kwargs):
        """Converts the HTML document (in request content) to the specified image format and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (required)
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

        all_params = ['out_path', 'out_format', 'file', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'resolution']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document_in_request_to_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` when calling `put_convert_document_in_request_to_image`")
        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `put_convert_document_in_request_to_image`")
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `put_convert_document_in_request_to_image`")

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
        # if 'file' in params:
        #     local_var_files['file'] = params['file']

        f = open(file,"rb")
        body_params = f.read()
        f.close()

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/octet-stream'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/convert/image/{outFormat}', 'PUT',
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

    def put_convert_document_in_request_to_pdf(self, out_path, file, **kwargs):
        """Converts the HTML document (in request content) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__put_convert_document_in_request_to_pdf_with_http_info(out_path, file, **kwargs)
        else:
            (data) = self.__put_convert_document_in_request_to_pdf_with_http_info(out_path, file, **kwargs)
            return data

    def __put_convert_document_in_request_to_pdf_with_http_info(self, out_path, file, **kwargs):
        """Converts the HTML document (in request content) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['out_path', 'file', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document_in_request_to_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` when calling `put_convert_document_in_request_to_pdf`")
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `put_convert_document_in_request_to_pdf`")

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

        f = open(file,"rb")
        body_params = f.read()
        f.close()

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/octet-stream'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/convert/pdf', 'PUT',
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

    def put_convert_document_in_request_to_xps(self, out_path, file, **kwargs):
        """Converts the HTML document (in request content) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__put_convert_document_in_request_to_xps_with_http_info(out_path, file, **kwargs)
        else:
            (data) = self.__put_convert_document_in_request_to_xps_with_http_info(out_path, file, **kwargs)
            return data

    def __put_convert_document_in_request_to_xps_with_http_info(self, out_path, file, **kwargs):
        """Converts the HTML document (in request content) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['out_path', 'file', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document_in_request_to_xps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'out_path' is set
        if ('out_path' not in params or
                params['out_path'] is None):
            raise ValueError("Missing the required parameter `out_path` when calling `put_convert_document_in_request_to_xps`")
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `put_convert_document_in_request_to_xps`")

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

        f = open(file,"rb")
        body_params = f.read()
        f.close()

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/octet-stream'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/convert/xps', 'PUT',
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

    def put_convert_document_to_image(self, name, out_path, out_format, **kwargs):
        """Converts the HTML document (located on storage) to the specified image format and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (required)
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
        if kwargs.get('async'):
            return self.__put_convert_document_to_image_with_http_info(name, out_path, out_format, **kwargs)
        else:
            (data) = self.__put_convert_document_to_image_with_http_info(name, out_path, out_format, **kwargs)
            return data

    def __put_convert_document_to_image_with_http_info(self, name, out_path, out_format, **kwargs):
        """Converts the HTML document (located on storage) to the specified image format and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.jpg) (required)
        :param str out_format: (required)
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

        all_params = ['name', 'out_path', 'out_format', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'resolution', 'folder', 'storage']
        all_params.append('async')
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/convert/image/{outFormat}', 'PUT',
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

    def put_convert_document_to_pdf(self, name, out_path, **kwargs):
        """Converts the HTML document (located on storage) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__put_convert_document_to_pdf_with_http_info(name, out_path, **kwargs)
        else:
            (data) = self.__put_convert_document_to_pdf_with_http_info(name, out_path, **kwargs)
            return data

    def __put_convert_document_to_pdf_with_http_info(self, name, out_path, **kwargs):
        """Converts the HTML document (located on storage) to PDF and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['name', 'out_path', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder', 'storage']
        all_params.append('async')
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/convert/pdf', 'PUT',
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

    def put_convert_document_to_xps(self, name, out_path, **kwargs):
        """Converts the HTML document (located on storage) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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
        if kwargs.get('async'):
            return self.__put_convert_document_to_xps_with_http_info(name, out_path, **kwargs)
        else:
            (data) = self.__put_convert_document_to_xps_with_http_info(name, out_path, **kwargs)
            return data

    def __put_convert_document_to_xps_with_http_info(self, name, out_path, **kwargs):
        """Converts the HTML document (located on storage) to XPS and uploads resulting file to storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
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

        all_params = ['name', 'out_path', 'width', 'height', 'left_margin', 'right_margin', 'top_margin', 'bottom_margin', 'folder', 'storage']
        all_params.append('async')
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/convert/xps', 'PUT',
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

##########################################################
#                 Document API
##########################################################

    def get_document(self, name, **kwargs):
        """Return the HTML document by the name from default or specified storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The document name. (required)
        :param str storage: The document folder
        :param str folder: The document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_document_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_document_with_http_info(name, **kwargs)
            return data

    def __get_document_with_http_info(self, name, **kwargs):
        """Return the HTML document by the name from default or specified storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The document name. (required)
        :param str storage: The document folder
        :param str folder: The document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'storage', 'folder']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_document`")

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
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
            ['multipart/form-data', 'application/zip'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}', 'GET',
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

    def get_document_fragment_by_x_path(self, name, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The document name. (required)
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :param str storage: The document storage.
        :param str folder: The document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_document_fragment_by_x_path_with_http_info(name, x_path, out_format, **kwargs)
        else:
            (data) = self.__get_document_fragment_by_x_path_with_http_info(name, x_path, out_format, **kwargs)
            return data

    def __get_document_fragment_by_x_path_with_http_info(self, name, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The document name. (required)
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :param str storage: The document storage.
        :param str folder: The document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'x_path', 'out_format', 'storage', 'folder']
        all_params.append('async')
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
            raise ValueError("Missing the required parameter `out_format` when calling `get_document_fragment_by_x_path`")

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/fragments/{outFormat}', 'GET',
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


    def get_document_fragment_by_x_path_by_url(self, source_url, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_document_fragment_by_x_path_by_url_with_http_info(source_url, x_path, out_format, **kwargs)
        else:
            (data) = self.__get_document_fragment_by_x_path_by_url_with_http_info(source_url, x_path, out_format, **kwargs)
            return data

    def __get_document_fragment_by_x_path_by_url_with_http_info(self, source_url, x_path, out_format, **kwargs):
        """Return list of HTML fragments matching the specified XPath query by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'x_path', 'out_format']
        all_params.append('async')
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
            raise ValueError("Missing the required parameter `source_url` when calling `get_document_fragment_by_x_path_by_url`")
        # verify the required parameter 'x_path' is set
        if ('x_path' not in params or
                params['x_path'] is None):
            raise ValueError("Missing the required parameter `x_path` when calling `get_document_fragment_by_x_path_by_url`")
        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `get_document_fragment_by_x_path_by_url`")

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/fragments/{outFormat}', 'GET',
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


    def get_document_images(self, name, **kwargs):
        """Return all HTML document images packaged as a ZIP archive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The document name. (required)
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_document_images_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_document_images_with_http_info(name, **kwargs)
            return data

    def __get_document_images_with_http_info(self, name, **kwargs):
        """Return all HTML document images packaged as a ZIP archive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The document name. (required)
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'folder', 'storage']
        all_params.append('async')
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/images/all', 'GET',
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

    def get_document_images_by_url(self, source_url, **kwargs):
        """Return all HTML page images packaged as a ZIP archive by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_document_images_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_document_images_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_document_images_by_url_with_http_info(self, source_url, **kwargs):
        """Return all HTML page images packaged as a ZIP archive by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url']
        all_params.append('async')
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/images/all', 'GET',
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

##########################################################
#                     OCR API
##########################################################

    def get_recognize_and_import_to_html(self, name, **kwargs):
        """Recognize text from the image file in the storage and import it to HTML format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The image file name. (required)
        :param str ocr_engine_lang: OCR engine language - language
        :param str folder: The source image folder.
        :param str storage: The source image storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_recognize_and_import_to_html_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_recognize_and_import_to_html_with_http_info(name, **kwargs)
            return data

    def __get_recognize_and_import_to_html_with_http_info(self, name, **kwargs):
        """Recognize text from the image file in the storage and import it to HTML format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The image file name. (required)
        :param str ocr_engine_lang: OCR engine language - language
        :param str folder: The source image folder.
        :param str storage: The source image storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'ocr_engine_lang', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recognize_and_import_to_html" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_recognize_and_import_to_html`")

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'ocr_engine_lang' in params:
            query_params.append(('ocrEngineLang', params['ocr_engine_lang']))
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
            '/html/{name}/ocr/import', 'GET',
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

    def get_recognize_and_translate_to_html(self, name, src_lang, res_lang, **kwargs):
        """Recognize text from the image file in the storage, import it to HTML format and translate to specified language.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The image file name. (required)
        :param str src_lang: Source language - also supposed as the OCR engine language. (required)
        :param str res_lang: Result language. (required)
        :param str folder: The source image folder.
        :param str storage: The source image storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_recognize_and_translate_to_html_with_http_info(name, src_lang, res_lang, **kwargs)
        else:
            (data) = self.__get_recognize_and_translate_to_html_with_http_info(name, src_lang, res_lang, **kwargs)
            return data

    def __get_recognize_and_translate_to_html_with_http_info(self, name, src_lang, res_lang, **kwargs):
        """Recognize text from the image file in the storage, import it to HTML format and translate to specified language.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: The image file name. (required)
        :param str src_lang: Source language - also supposed as the OCR engine language. (required)
        :param str res_lang: Result language. (required)
        :param str folder: The source image folder.
        :param str storage: The source image storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'src_lang', 'res_lang', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recognize_and_translate_to_html" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_recognize_and_translate_to_html`")
        # verify the required parameter 'src_lang' is set
        if ('src_lang' not in params or
                params['src_lang'] is None):
            raise ValueError("Missing the required parameter `src_lang` when calling `get_recognize_and_translate_to_html`")
        # verify the required parameter 'res_lang' is set
        if ('res_lang' not in params or
                params['res_lang'] is None):
            raise ValueError("Missing the required parameter `res_lang` when calling `get_recognize_and_translate_to_html`")

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'src_lang' in params:
            path_params['srcLang'] = params['src_lang']
        if 'res_lang' in params:
            path_params['resLang'] = params['res_lang']

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/ocr/translate/{srcLang}/{resLang}', 'GET',
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

##########################################################
#                 Translation API
##########################################################

    def get_translate_document(self, name, src_lang, res_lang, **kwargs):
        """Translate the HTML document specified by the name from default or specified storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str src_lang: Source language. (required)
        :param str res_lang: Result language. (required)
        :param str storage: The source document storage.
        :param str folder: The source document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_translate_document_with_http_info(name, src_lang, res_lang, **kwargs)
        else:
            (data) = self.__get_translate_document_with_http_info(name, src_lang, res_lang, **kwargs)
            return data

    def __get_translate_document_with_http_info(self, name, src_lang, res_lang, **kwargs):
        """Translate the HTML document specified by the name from default or specified storage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str src_lang: Source language. (required)
        :param str res_lang: Result language. (required)
        :param str storage: The source document storage.
        :param str folder: The source document folder.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'src_lang', 'res_lang', 'storage', 'folder']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_translate_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_translate_document`")
        # verify the required parameter 'src_lang' is set
        if ('src_lang' not in params or
                params['src_lang'] is None):
            raise ValueError("Missing the required parameter `src_lang` when calling `get_translate_document`")
        # verify the required parameter 'res_lang' is set
        if ('res_lang' not in params or
                params['res_lang'] is None):
            raise ValueError("Missing the required parameter `res_lang` when calling `get_translate_document`")

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'src_lang' in params:
            path_params['srcLang'] = params['src_lang']
        if 'res_lang' in params:
            path_params['resLang'] = params['res_lang']

        query_params = []
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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/translate/{srcLang}/{resLang}', 'GET',
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

    def get_translate_document_by_url(self, source_url, src_lang, res_lang, **kwargs):
        """Translate the HTML document from Web specified by its URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source document URL. (required)
        :param str src_lang: Source language. (required)
        :param str res_lang: Result language. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_translate_document_by_url_with_http_info(source_url, src_lang, res_lang, **kwargs)
        else:
            (data) = self.__get_translate_document_by_url_with_http_info(source_url, src_lang, res_lang, **kwargs)
            return data

    def __get_translate_document_by_url_with_http_info(self, source_url, src_lang, res_lang, **kwargs):
        """Translate the HTML document from Web specified by its URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source document URL. (required)
        :param str src_lang: Source language. (required)
        :param str res_lang: Result language. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url', 'src_lang', 'res_lang']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_translate_document_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `get_translate_document_by_url`")
        # verify the required parameter 'src_lang' is set
        if ('src_lang' not in params or
                params['src_lang'] is None):
            raise ValueError("Missing the required parameter `src_lang` when calling `get_translate_document_by_url`")
        # verify the required parameter 'res_lang' is set
        if ('res_lang' not in params or
                params['res_lang'] is None):
            raise ValueError("Missing the required parameter `res_lang` when calling `get_translate_document_by_url`")

        collection_formats = {}

        path_params = {}
        if 'src_lang' in params:
            path_params['srcLang'] = params['src_lang']
        if 'res_lang' in params:
            path_params['resLang'] = params['res_lang']

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/translate/{srcLang}/{resLang}', 'GET',
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

##########################################################
#                  Summarization API
##########################################################

    def get_detect_html_keywords(self, name, **kwargs):
        """Get the HTML document keywords using the keyword detection service.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str folder: Document folder.
        :param str storage: Document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_detect_html_keywords_with_http_info(name, **kwargs)
        else:
            (data) = self.__get_detect_html_keywords_with_http_info(name, **kwargs)
            return data

    def __get_detect_html_keywords_with_http_info(self, name, **kwargs):
        """Get the HTML document keywords using the keyword detection service.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str name: Document name. (required)
        :param str folder: Document folder.
        :param str storage: Document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['name', 'folder', 'storage']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_detect_html_keywords" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_detect_html_keywords`")

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
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/{name}/summ/keywords', 'GET',
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

    def get_detect_html_keywords_by_url(self, source_url, **kwargs):
        """Get the keywords from HTML document from Web specified by its URL using the keyword detection service

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source document URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.__get_detect_html_keywords_by_url_with_http_info(source_url, **kwargs)
        else:
            (data) = self.__get_detect_html_keywords_by_url_with_http_info(source_url, **kwargs)
            return data

    def __get_detect_html_keywords_by_url_with_http_info(self, source_url, **kwargs):
        """Get the keywords from HTML document from Web specified by its URL using the keyword detection service

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param bool async: Asynchronous request
        :param str source_url: Source document URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['source_url']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_detect_html_keywords_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `get_detect_html_keywords_by_url`")

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
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/html/summ/keywords', 'GET',
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

