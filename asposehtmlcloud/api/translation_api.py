# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="translation_api.py">
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


class TranslationApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def translation_get_translate_document(self, name, src_lang, res_lang, **kwargs):
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
            return self.__translation_get_translate_document_with_http_info(name, src_lang, res_lang, **kwargs)
        else:
            (data) = self.__translation_get_translate_document_with_http_info(name, src_lang, res_lang, **kwargs)
            return data

    def __translation_get_translate_document_with_http_info(self, name, src_lang, res_lang, **kwargs):
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
                    " to method translation_get_translate_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `translation_get_translate_document`")
        # verify the required parameter 'src_lang' is set
        if ('src_lang' not in params or
                params['src_lang'] is None):
            raise ValueError("Missing the required parameter `src_lang` when calling `translation_get_translate_document`")
        # verify the required parameter 'res_lang' is set
        if ('res_lang' not in params or
                params['res_lang'] is None):
            raise ValueError("Missing the required parameter `res_lang` when calling `translation_get_translate_document`")

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

    def translation_get_translate_document_by_url(self, source_url, src_lang, res_lang, **kwargs):
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
            return self.__translation_get_translate_document_by_url_with_http_info(source_url, src_lang, res_lang, **kwargs)
        else:
            (data) = self.__translation_get_translate_document_by_url_with_http_info(source_url, src_lang, res_lang, **kwargs)
            return data

    def __translation_get_translate_document_by_url_with_http_info(self, source_url, src_lang, res_lang, **kwargs):
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
                    " to method translation_get_translate_document_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_url' is set
        if ('source_url' not in params or
                params['source_url'] is None):
            raise ValueError("Missing the required parameter `source_url` when calling `translation_get_translate_document_by_url`")
        # verify the required parameter 'src_lang' is set
        if ('src_lang' not in params or
                params['src_lang'] is None):
            raise ValueError("Missing the required parameter `src_lang` when calling `translation_get_translate_document_by_url`")
        # verify the required parameter 'res_lang' is set
        if ('res_lang' not in params or
                params['res_lang'] is None):
            raise ValueError("Missing the required parameter `res_lang` when calling `translation_get_translate_document_by_url`")

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

