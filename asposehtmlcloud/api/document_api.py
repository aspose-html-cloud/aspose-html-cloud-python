# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="document_api.py">
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

# python 2 and python 3 compatibility library
import six

from asposehtmlcloud.api_client import ApiClient


class DocumentApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def document_get_document(self, name, **kwargs):
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
            return self.__document_get_document_with_http_info(name, **kwargs)
        else:
            (data) = self.__document_get_document_with_http_info(name, **kwargs)
            return data

    def __document_get_document_with_http_info(self, name, **kwargs):
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
                    " to method document_get_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `document_get_document`")

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

    def document_get_document_fragment_by_x_path(self, name, x_path, out_format, **kwargs):
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
            return self.__document_get_document_fragment_by_x_path_with_http_info(name, x_path, out_format, **kwargs)
        else:
            (data) = self.__document_get_document_fragment_by_x_path_with_http_info(name, x_path, out_format, **kwargs)
            return data

    def __document_get_document_fragment_by_x_path_with_http_info(self, name, x_path, out_format, **kwargs):
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
                    " to method document_get_document_fragment_by_x_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `document_get_document_fragment_by_x_path`")
        # verify the required parameter 'x_path' is set
        if ('x_path' not in params or
                params['x_path'] is None):
            raise ValueError("Missing the required parameter `x_path` when calling `document_get_document_fragment_by_x_path`")
        # verify the required parameter 'out_format' is set
        if ('out_format' not in params or
                params['out_format'] is None):
            raise ValueError("Missing the required parameter `out_format` when calling `document_get_document_fragment_by_x_path`")

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

    def document_get_document_images(self, name, **kwargs):
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
            return self.__document_get_document_images_with_http_info(name, **kwargs)
        else:
            (data) = self.__document_get_document_images_with_http_info(name, **kwargs)
            return data

    def __document_get_document_images_with_http_info(self, name, **kwargs):
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
                    " to method document_get_document_images" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `document_get_document_images`")

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
