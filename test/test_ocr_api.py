# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_ocr_api.py">
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
from asposehtmlcloud.api.ocr_api import OcrApi
from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestOcrApi(unittest.TestCase):

    def setUp(self):
        self.api = OcrApi()

    def test_ocr_get_recognize_and_import_to_html(self):
        """Test case for ocr_get_recognize_and_import_to_html

        Recognize text from the image file in the storage and import it to HTML format.

        param async bool
        param str name: The image file name. (required)
        param str ocr_engine_lang: OCR engine language - language
        param str folder: The source image folder.
        param str storage: The source image storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        file_name = "test_ocr.png"
        lang = "en"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(file_name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Recognize image
            res = self.api.ocr_get_recognize_and_import_to_html(
                file_name, ocr_engine_lang=lang, folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error OCR test")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_ocr_get_recognize_and_translate_to_html(self):
        """Test case for ocr_get_recognize_and_translate_to_html

        Recognize text from the image file in the storage, import it to HTML format and translate to specified language.

        param async bool
        param str name: The image file name. (required)
        param str src_lang: Source language - also supposed as the OCR engine language. (required)
        param str res_lang: Result language. (required)
        param str folder: The source image folder.
        param str storage: The source image storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        file_name = "test_ocr.jpg"
        src_lang = "en"
        res_lang = "de"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(file_name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Recognize and translate image
            res = self.api.ocr_get_recognize_and_translate_to_html(file_name, src_lang, res_lang, folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error OCR and translate test")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
