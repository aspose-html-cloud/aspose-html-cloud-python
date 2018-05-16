# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_translation_api.py">
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
import unittest
from asposehtmlcloud.api.translation_api import TranslationApi
from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestTranslationApi(unittest.TestCase):

    def setUp(self):
        self.api = TranslationApi()

    def test_translation_get_translate_document(self):
        """Test case for translation_get_translate_document

        Translate the HTML document specified by the name from default or specified storage.

        param async bool
        param str name: Document name. (required)
        param str src_lang: Source language. (required)
        param str res_lang: Result language. (required)
        param str storage: The source document storage.
        param str folder: The source document folder.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        file_name = "test_en.html"
        src_lang = "en"
        res_lang = "de"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(file_name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Translate document
            res = self.api.translation_get_translate_document(file_name, src_lang, res_lang,
                                                              folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error translate html document")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_translation_get_translate_document_by_url(self):
        """Test case for translation_get_translate_document_by_url

        Translate the HTML document from Web specified by its URL.

        param async bool
        param str source_url: Source document URL. (required)
        param str src_lang: Source language. (required)
        param str res_lang: Result language. (required)
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        source_url = "https://www.le.ac.uk/oerresources/bdra/html/page_02.htm"
        src_lang = "en"
        res_lang = "fr"
        try:
            # Translate url
            res = self.api.translation_get_translate_document_by_url(source_url, src_lang, res_lang)
            self.assertTrue(isinstance(res, str), "Error translate document from url")

            # Move to test folder
            TestHelper.move_file(res, TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main(verbosity=2)
