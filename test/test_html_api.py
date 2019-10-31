# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_html_api.py">
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
import unittest
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestHtmlApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TestHelper.html

###############################################################
#                    Conversion test
###############################################################

    def test_get_convert_html_to_image(self):
        """Test case for get_convert_document_to_image from html format

        Convert the HTML document from the storage by its name to the specified image format.

        param async_req bool
        param str name: Document name. (required)
        param str out_format: Resulting image format. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param int resolution: Resolution of resulting image.
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
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to image
            res = self.api.get_convert_document_to_image(
                name, out_format="png", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert document to image")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_epub_to_image(self):
        """Test case for get_convert_document_to_image from epub format

        Convert the EPUB document from the storage by its name to the specified image format.

        param async_req bool
        param str name: Document name. (required)
        param str out_format: Resulting image format. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param int resolution: Resolution of resulting image.
        param str folder: The source document folder.
        param str storage: The source document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "georgia.epub"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to image
            res = self.api.get_convert_document_to_image(
                name, out_format="jpeg", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert epub to jpeg")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_svg_to_image(self):
        """Test case for get_convert_document_to_image from svg format

        Convert the SVG document from the storage by its name to the specified image format.

        param async_req bool
        param str name: Document name. (required)
        param str out_format: Resulting image format. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param int resolution: Resolution of resulting image.
        param str folder: The source document folder.
        param str storage: The source document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "Map-World.svg"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to image
            res = self.api.get_convert_document_to_image(
                name, out_format="bmp", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert svg to bmp")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_html_to_image_by_url(self):
        """Test case for get_convert_document_to_image_by_url

        Convert the HTML page from the web by its URL to the specified image format.

        param async_req bool
        param str source_url: Source page URL. (required)
        param str out_format: Resulting image format. (required)
        param int width: Resulting image width.
        param int height: Resulting image height.
        param int left_margin: Left resulting image margin.
        param int right_margin: Right resulting image margin.
        param int top_margin: Top resulting image margin.
        param int bottom_margin: Bottom resulting image margin.
        param int resolution: Resolution of resulting image.
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
        try:

            # Convert url to image
            res = self.api.get_convert_document_to_image_by_url(
                source_url, out_format="jpeg", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert url to image")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_html_to_pdf(self):
        """Test case for get_convert_document_to_pdf from html format

        Convert the HTML document from the storage by its name to PDF.

        param async_req bool
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
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to pdf
            res = self.api.get_convert_document_to_pdf(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert html to pdf")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_epub_to_pdf(self):
        """Test case for get_convert_document_to_pdf from epub format

        Convert the EPUB document from the storage by its name to PDF.

        param async_req bool
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
        name = "georgia.epub"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to pdf
            res = self.api.get_convert_document_to_pdf(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert epub to pdf")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_svg_to_pdf(self):
        """Test case for get_convert_document_to_pdf from svg format

        Convert the SVG document from the storage by its name to PDF.

        param async_req bool
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
        name = "Map-World.svg"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to pdf
            res = self.api.get_convert_document_to_pdf(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert svg to pdf")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_html_to_pdf_by_url(self):
        """Test case for get_convert_document_to_pdf_by_url

        Convert the HTML page from the web by its URL to PDF.

        param async_req bool
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
            res = self.api.get_convert_document_to_pdf_by_url(
                source_url, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150,
                bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert url to pdf")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_html_to_xps(self):
        """Test case for get_convert_document_to_xps from html format

        Convert the HTML document from the storage by its name to XPS.

        param async_req bool
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
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to xps
            res = self.api.get_convert_document_to_xps(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert html to xps")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_epub_to_xps(self):
        """Test case for get_convert_document_to_xps from epub format

        Convert the EPUB document from the storage by its name to XPS.

        param async_req bool
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
        name = "georgia.epub"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to xps
            res = self.api.get_convert_document_to_xps(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert epub to xps")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_svg_to_xps(self):
        """Test case for get_convert_document_to_xps from svg format

        Convert the SVG document from the storage by its name to XPS.

        param async_req bool
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
        name = "Map-World.svg"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to xps
            res = self.api.get_convert_document_to_xps(
                name, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150, bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert svg to xps")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_html_to_xps_by_url(self):
        """Test case for get_convert_document_to_xps_by_url

        Convert the HTML page from the web by its URL to XPS.

        param async_req bool
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
            res = self.api.get_convert_document_to_xps_by_url(
                source_url, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150,
                bottom_margin=200, folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert url to xps")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_html_in_request_to_image(self):
        """Test case for post_convert_document_in_request_to_image from html format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postHtmlToImageInReq.png"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "test1.html"

        try:
            # Convert document to image
            self.api.post_convert_document_in_request_to_image(
                out_path=test_out_path, out_format="png", file=test_file, width=800, height=1000, left_margin=50,
                right_margin=100, top_margin=150, bottom_margin=200, resolution=300)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_epub_in_request_to_image(self):
        """Test case for post_convert_document_in_request_to_image from epub format

        :param async_req bool
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
        :return: File.
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postEpubToImageInReq.zip"
        result_file_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "georgia.epub"

        try:
            # Convert document to image
            self.api.post_convert_document_in_request_to_image(
                out_path=result_file_path, out_format="jpeg", file=test_file, width=800, height=1000, left_margin=50,
                right_margin=100, top_margin=150, bottom_margin=200, resolution=300)

            # Download result
            res = TestHelper.download_file(result_file_path)

            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_svg_in_request_to_image(self):
        """Test case for post_convert_document_in_request_to_image from svg format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postSvgToImageInReq.jpg"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "Map-World.svg"

        try:
            # Convert document to image
            self.api.post_convert_document_in_request_to_image(
                out_path=test_out_path, out_format="jpeg", file=test_file, width=800, height=1000, left_margin=50,
                right_margin=100, top_margin=150, bottom_margin=200, resolution=300)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_html_in_request_to_pdf(self):
        """Test case for post_convert_document_in_request_to_pdf from html format

        :param async_req bool
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.pdf) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postHtmlToPdfInReq.pdf"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "test1.html"
        try:
            # Upload and convert document to pdf
            self.api.post_convert_document_in_request_to_pdf(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_epub_in_request_to_pdf(self):
        """Test case for post_convert_document_in_request_to_pdf from epub format

        :param async_req bool
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.pdf) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postEpubToPdfInReq.pdf"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "georgia.epub"
        try:
            # Upload and convert document to pdf
            self.api.post_convert_document_in_request_to_pdf(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_svg_in_request_to_pdf(self):
        """Test case for post_convert_document_in_request_to_pdf from svg format

        :param async_req bool
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.pdf) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postSvgToPdfInReq.pdf"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "Map-World.svg"
        try:
            # Upload and convert document to pdf
            self.api.post_convert_document_in_request_to_pdf(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_html_in_request_to_xps(self):
        """Test case for post_convert_document_in_request_to_xps from html format

        :param async_req bool
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.xps) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postHtmlToXpsInReq.xps"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "test1.html"
        try:
            # Upload and convert document to xps
            self.api.post_convert_document_in_request_to_xps(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_epub_in_request_to_xps(self):
        """Test case for post_convert_document_in_request_to_xps from epub format

        :param async_req bool
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.xps) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postEpubToXpsInReq.xps"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "georgia.epub"
        try:
            # Upload and convert document to xps
            self.api.post_convert_document_in_request_to_xps(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_svg_in_request_to_xps(self):
        """Test case for post_convert_document_in_request_to_xps from svg format

        :param async_req bool
        :param str out_path: Full resulting filename (ex. /folder1/folder2/result.xps) (required)
        :param file file: A file to be converted. (required)
        :param int width: Resulting document page width in points (1/96 inch).
        :param int height: Resulting document page height in points (1/96 inch).
        :param int left_margin: Left resulting document page margin in points (1/96 inch).
        :param int right_margin: Right resulting document page margin in points (1/96 inch).
        :param int top_margin: Top resulting document page margin in points (1/96 inch).
        :param int bottom_margin: Bottom resulting document page margin in points (1/96 inch).
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "postSvgToXpsInReq.xps"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "Map-World.svg"
        try:
            # Upload and convert document to xps
            self.api.post_convert_document_in_request_to_xps(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_html_to_image(self):
        """Test case for put_convert_document_to_image from html format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "test1.html"
        result_name = "putHtmlToImg.tiff"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to image in storage
            self.api.put_convert_document_to_image(
                name, out_path=test_out_path, out_format="tiff", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_epub_to_image(self):
        """Test case for put_convert_document_to_image from epub format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "georgia.epub"
        result_name = "putEpubToTiff.zip"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to image in storage
            self.api.put_convert_document_to_image(
                name, out_path=test_out_path, out_format="tiff", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_svg_to_image(self):
        """Test case for put_convert_document_to_image from svg format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "Map-World.svg"
        result_name = "putSvgToImg.tiff"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to image in storage
            self.api.put_convert_document_to_image(
                name, out_path=test_out_path, out_format="tiff", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_html_to_pdf(self):
        """Test case for put_convert_document_to_pdf from html format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "test1.html"
        result_name = "putHtmlToPdf.pdf"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to pdf in storage
            self.api.put_convert_document_to_pdf(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_epub_to_pdf(self):
        """Test case for put_convert_document_to_pdf from epub format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "georgia.epub"
        result_name = "putEpubToPdf.pdf"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to pdf in storage
            self.api.put_convert_document_to_pdf(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_svg_to_pdf(self):
        """Test case for put_convert_document_to_pdf from svg format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "Map-World.svg"
        result_name = "putSvgToPdf.pdf"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to pdf in storage
            self.api.put_convert_document_to_pdf(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_html_to_xps(self):
        """Test case for put_convert_document_to_xps from html format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "test1.html"
        result_name = "putHtmlToXps.xps"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to pdf in storage
            self.api.put_convert_document_to_xps(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_epub_to_xps(self):
        """Test case for put_convert_document_to_xps from epub format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "georgia.epub"
        result_name = "putEpubToXps.xps"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to pdf in storage
            self.api.put_convert_document_to_xps(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_svg_to_xps(self):
        """Test case for put_convert_document_to_xps from svg format

        :param async_req bool
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
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # Already in storage
        name = "Map-World.svg"
        result_name = "putSvgToXps.xps"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to pdf in storage
            self.api.put_convert_document_to_xps(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_html_to_mhtml_by_url(self):
        """Test case for get_convert_document_to_mhtml_by_url

        Converts the HTML page from Web by its URL to MHTML returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        source_url = "https://www.yahoo.com/"
        try:

            # Get document by url and convert to mhtml
            res = self.api.get_convert_document_to_mhtml_by_url(source_url=source_url)
            self.assertTrue(isinstance(res, str), "Error get site")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_convert_html_to_markdown(self):
        """Test case for get_convert_document_to_markdown

        Converts the HTML document (located on storage) to Markdown and returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :param str folder: Source document folder.
        :param str storage: Source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        name = "test_md.html"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert document to markdown
            res = self.api.get_convert_document_to_markdown(name,
                                                            use_git="true",
                                                            folder=TestHelper.folder,
                                                            storage="")
            self.assertTrue(isinstance(res, str), "Error convert document to markdown")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_html_in_request_to_markdown(self):
        """Test case for post_convert_document_in_request_to_markdown

        Converts the HTML document (in request content) to Markdown and uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.md) (required)
        :param file file: A file to be converted. (required)
        :param str use_git: Use Git Markdown flavor to save ("true" or "false").
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        name = "postConvertToMarkdownInReqPy.md"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "test_md.html"
        try:

            # Upload and convert document to markdown
            self.api.post_convert_document_in_request_to_markdown(
                out_path=test_out_path, file=test_file, use_git="true")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_html_to_markdown(self):
        """Test case for put_convert_document_to_markdown

        Converts the HTML document (located on storage) to Markdown and uploads resulting file to storage by specified path.

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
        # Already in storage
        name = "test_md.html"
        result_name = "putConvertToMarkdownPy.md"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to markdown in storage
            self.api.put_convert_document_to_markdown(
                name, out_path=test_out_path, use_git="false", folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    ###############################################################
    #                    Import test
    ###############################################################

    def test_get_convert_markdown_to_html(self):
        """Test case for get_convert_markdown_to_html

        Converts the HTML Markdown (located on storage) to HTML and
        returns resulting file in response content.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: Document name. (required)
        :param str folder: Source document folder.
        :param str storage: Source document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        name = "testpage1.md"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Convert markdown to html
            res = self.api.get_convert_markdown_to_html(name,
                                                        folder=TestHelper.folder,
                                                        storage="")
            self.assertTrue(isinstance(res, str), "Error convert markdown to html")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_convert_markdown_in_request_to_html(self):
        """Test case for post_convert_markdown_in_request_to_html

        Converts the Markdown document (in request content) to HTML and
        uploads resulting file to storage by specified path.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str out_path: Full resulting file path in the storage (ex. /folder1/folder2/result.html) (required)
        :param file file: A file to be converted. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        name = "postMarkdownToHtmlInReqPy.html"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "testpage1.md"
        try:

            # Upload and convert document to markdown
            self.api.post_convert_markdown_in_request_to_html(
                out_path=test_out_path, file=test_file)

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_put_convert_markdown_to_html(self):
        """Test case for put_convert_markdown_to_html

        Converts the Markdown document (located on storage) to HTML
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
        # Already in storage
        name = "testpage1.md"
        result_name = "putMarkdownToHtmlPy.html"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:
            # Convert document to markdown in storage
            self.api.put_convert_markdown_to_html(
                name, out_path=test_out_path, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(test_out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    ###############################################################
    #                    Document test
    ###############################################################

    def test_get_document_by_url(self):
        """Test case for get_document_by_url

        Return all HTML page with linked resources packaged as a ZIP archive by the source page URL.

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """
        source_url = "https://lenta.ru/"
        try:

            # Get site by url
            res = self.api.get_document_by_url(source_url=source_url)
            self.assertTrue(isinstance(res, str), "Error get site")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_document_fragment_by_x_path(self):

        """Test case for get_document_fragment_by_x_path

        Return list of HTML fragments matching the specified XPath query.

        param async_req bool
        param str name: The document name. (required)
        param str x_path: XPath query string. (required)
        param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        param str storage: The document storage.
        param str folder: The document folder.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "test2.html.zip"
        x_path = ".//p"
        out_format = "plain"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Get fragment document from remote storage
            res = self.api.get_document_fragment_by_x_path(name=name, x_path=x_path, out_format=out_format,
                                                           storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get fragment document from remote storage")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_document_fragment_by_x_path_by_url(self):

        """Return list of HTML fragments matching the specified XPath query by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str x_path: XPath query string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        source_url = "https://stallman.org/articles/anonymous-payments-thru-phones.html"
        x_path = ".//p"
        out_format = "plain"
        try:
            # Get fragment document from remote storage by url
            res = self.api.get_document_fragment_by_x_path_by_url(source_url=source_url, x_path=x_path, out_format=out_format)
            self.assertTrue(isinstance(res, str), "Error get fragment document from remote storage by url")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_document_fragments_by_css_selector(self):

        """Return list of HTML fragments matching the specified CSS selector.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str name: The document name. (required)
        :param str selector: CSS selector string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :param str folder: The document folder.
        :param str storage: The document storage.
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        name = "test2.html.zip"
        selector = "div p"
        out_format = "plain"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Get fragment document from remote storage by css
            res = self.api.get_document_fragments_by_css_selector(name=name, selector=selector, out_format=out_format,
                                                                  storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get fragment document from remote storage")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_document_fragments_by_css_selector_by_url(self):

        """Return list of HTML fragments matching the specified CSS selector by the source page URL.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str source_url: Source page URL. (required)
        :param str selector: CSS selector string. (required)
        :param str out_format: Output format. Possible values: 'plain' and 'json'. (required)
        :return: File. If the method is called asynchronously, returns the request thread.
        """

        source_url = "https://www.w3schools.com/cssref/css_selectors.asp"
        selector = 'a[href$=".asp"]' # Get all asp links
        out_format = "plain"
        try:
            # Get fragment matching the specified CSS selector by url
            res = self.api.get_document_fragments_by_css_selector_by_url(source_url=source_url, selector=selector, out_format=out_format)
            self.assertTrue(isinstance(res, str), "Error get fragment matching the specified CSS selector by url")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_document_images(self):
        """Test case for get_document_images

        Return all HTML document images packaged as a ZIP archive.

        param async_req bool
        param str name: The document name. (required)
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "test3.html.zip"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Get images from document on remote storage
            res = self.api.get_document_images(name=name, storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get images from document")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_document_images_by_url(self):
        """Test case for get_document_images

        Return all HTML document images packaged as a ZIP archive.

        param async_req bool
        param str name: The document name. (required)
        param str folder: The document folder.
        param str storage: The document storage.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        source_url = "https://www.google.com/"
        try:
            # Get images from document by url
            res = self.api.get_document_images_by_url(source_url=source_url)
            self.assertTrue(isinstance(res, str), "Error get images from url")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    ###############################################################
    #               TemplateMerge test
    ###############################################################

    def test_get_merge_html_template(self):
        """Test case for put_convert_document_in_request_to_image

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

        template_name = "HtmlTemplate.html"
        template_data = "XmlSourceData.xml"
        result_name = "GetTemplateMergePython.html"
        options = ""
        folder = "HtmlTestDoc"
        storage = ""
        data_path = folder + "/" + template_data

        try:
            res = TestHelper.upload_file(template_name)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            res = TestHelper.upload_file(template_data)
            self.assertTrue(len(res.uploaded) == 1)
            self.assertTrue(len(res.errors) == 0)

            # Get result file from storage
            res = self.api.get_merge_html_template(template_name=template_name,data_path=data_path,options=options,
                                                   folder=folder, storage=storage)
            self.assertTrue(isinstance(res, str), "Error merge template")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst + result_name)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_post_merge_html_template(self):
        """Test case for post_convert_document_in_request_to_image

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
        template_name = "HtmlTemplate.html"
        template_data = "XmlSourceData.xml"
        result_name = "PostMergeHtmlTemplatePython.html"
        options = ""
        folder = "HtmlTestDoc"
        storage = ""
        data_file = TestHelper.test_src + template_data
        out_path = folder + "/" + result_name

        try:
            # Convert document to image
            self.api.post_merge_html_template(template_name=template_name, out_path=out_path, file=data_file,
                                             options=options, folder=folder, storage=storage)
            # Download result
            res = TestHelper.download_file(out_path)
            save_file = TestHelper.test_dst + result_name
            TestHelper.move_file(res, save_file)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
