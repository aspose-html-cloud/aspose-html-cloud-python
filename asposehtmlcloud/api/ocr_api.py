# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="ocr_api.py">
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


class OcrApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ocr_get_recognize_and_import_to_html(self, name, **kwargs):
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
            return self.__ocr_get_recognize_and_import_to_html_with_http_info(name, **kwargs)
        else:
            (data) = self.__ocr_get_recognize_and_import_to_html_with_http_info(name, **kwargs)
            return data

    def __ocr_get_recognize_and_import_to_html_with_http_info(self, name, **kwargs):
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
                    " to method ocr_get_recognize_and_import_to_html" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `ocr_get_recognize_and_import_to_html`")

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

    def ocr_get_recognize_and_translate_to_html(self, name, src_lang, res_lang, **kwargs):
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
            return self.__ocr_get_recognize_and_translate_to_html_with_http_info(name, src_lang, res_lang, **kwargs)
        else:
            (data) = self.__ocr_get_recognize_and_translate_to_html_with_http_info(name, src_lang, res_lang, **kwargs)
            return data

    def __ocr_get_recognize_and_translate_to_html_with_http_info(self, name, src_lang, res_lang, **kwargs):
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
                    " to method ocr_get_recognize_and_translate_to_html" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `ocr_get_recognize_and_translate_to_html`")
        # verify the required parameter 'src_lang' is set
        if ('src_lang' not in params or
                params['src_lang'] is None):
            raise ValueError("Missing the required parameter `src_lang` when calling `ocr_get_recognize_and_translate_to_html`")
        # verify the required parameter 'res_lang' is set
        if ('res_lang' not in params or
                params['res_lang'] is None):
            raise ValueError("Missing the required parameter `res_lang` when calling `ocr_get_recognize_and_translate_to_html`")

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
