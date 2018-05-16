# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_conversion_api.py">
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

from asposehtmlcloud.api.conversion_api import ConversionApi
from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestConversionApi(unittest.TestCase):

    def setUp(self):
        self.api = ConversionApi()

#    @unittest.skip("skipping")
    def test_conversion_get_convert_document_to_image(self):
        """Test case for conversion_get_convert_document_to_image

        Convert the HTML document from the storage by its name to the specified image format.

        param async bool
        param str name: Document name. (required)
        param str out_format: Resulting image format. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param int x_resolution: Horizontal resolution of resulting image.
        param int y_resolution: Vertical resolution of resulting image.
        param str folder: The source document folder.
        param str storage: The source document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        name = "test1.html"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Convert document to image
            res = self.api.conversion_get_convert_document_to_image(
                name, out_format="png", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, x_resolution=300, y_resolution=300,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert document to image")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_conversion_get_convert_document_to_image_by_url(self):
        """Test case for conversion_get_convert_document_to_image_by_url

        Convert the HTML page from the web by its URL to the specified image format.

        param async bool
        param str source_url: Source page URL. (required)
        param str out_format: Resulting image format. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param int x_resolution: Horizontal resolution of resulting image.
        param int y_resolution: Vertical resolution of resulting image.
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
        try:

            # Convert url to image
            res = self.api.conversion_get_convert_document_to_image_by_url(
                source_url, out_format="jpeg", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, x_resolution=300, y_resolution=300,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert url to image")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_conversion_get_convert_document_to_pdf(self):
        """Test case for conversion_get_convert_document_to_pdf

        Convert the HTML document from the storage by its name to PDF.

        param async bool
        param str name: Document name. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        name = "test1.html"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Convert document to pdf
            res = self.api.conversion_get_convert_document_to_pdf(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert document to pdf")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_conversion_get_convert_document_to_pdf_by_url(self):
        """Test case for conversion_get_convert_document_to_pdf_by_url

        Convert the HTML page from the web by its URL to PDF.

        param async bool
        param str source_url: Source page URL. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
        try:

            # Convert url to pdf
            res = self.api.conversion_get_convert_document_to_pdf_by_url(
                source_url, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert url to pdf")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_conversion_get_convert_document_to_xps(self):
        """Test case for conversion_get_convert_document_to_xps

        Convert the HTML document from the storage by its name to XPS.

        param async bool
        param str name: Document name. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        name = "test1.html"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Convert document to xps
            res = self.api.conversion_get_convert_document_to_xps(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert document to xps")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_conversion_get_convert_document_to_xps_by_url(self):
        """Test case for conversion_get_convert_document_to_xps_by_url

        Convert the HTML page from the web by its URL to XPS.

        param async bool
        param str source_url: Source page URL. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.

        """
        source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
        try:

            # Convert url to xps
            res = self.api.conversion_get_convert_document_to_xps_by_url(
                source_url, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert url to xps")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
