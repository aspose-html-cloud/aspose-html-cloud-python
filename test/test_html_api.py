# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_html_api.py">
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

from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestDocumentApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        configuration = Configuration(apiKey="",
                                      appSid="",
                                      basePath="https://api.aspose.cloud/v1.1",
                                      authPath="https://api.aspose.cloud/oauth2/token",
                                      debug=True)
        cls.api = HtmlApi(configuration)

###############################################################
#                    Conversion test
###############################################################

    #    @unittest.skip("skipping")
    def test_get_convert_document_to_image(self):
        """Test case for get_convert_document_to_image

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
            res = self.api.get_convert_document_to_image(
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
    def test_get_convert_document_to_image_by_url(self):
        """Test case for get_convert_document_to_image_by_url

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
            res = self.api.get_convert_document_to_image_by_url(
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
    def test_get_convert_document_to_pdf(self):
        """Test case for get_convert_document_to_pdf

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
            res = self.api.get_convert_document_to_pdf(
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
    def test_get_convert_document_to_pdf_by_url(self):
        """Test case for get_convert_document_to_pdf_by_url

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

    #    @unittest.skip("skipping")
    def test_get_convert_document_to_xps(self):
        """Test case for get_convert_document_to_xps

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
            res = self.api.get_convert_document_to_xps(
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
    def test_get_convert_document_to_xps_by_url(self):
        """Test case for get_convert_document_to_xps_by_url

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
            res = self.api.get_convert_document_to_xps_by_url(
                source_url, width=800, height=1000, left_margin=50, right_margin=100, top_margin=150,
                bottom_margin=200,
                folder=TestHelper.folder, storage=""
            )
            self.assertTrue(isinstance(res, str), "Error convert url to xps")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    #    @unittest.skip("skipping")
    def test_put_convert_document_in_request_to_image(self):
        """Test case for put_convert_document_in_request_to_image

        :param async bool
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
        name = "putConvertToImage.png"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "test1.html"

        try:
            # Convert document to image
            self.api.put_convert_document_in_request_to_image(
                out_path=test_out_path, out_format="png", file=test_file, width=800, height=1000, left_margin=50,
                right_margin=100, top_margin=150, bottom_margin=200, resolution=300)

            # Download result
            res = TestHelper.download_file(name)

            save_file = TestHelper.test_dst + name

            # Save to test folder
            with open(save_file, "wb") as file:
                file.write(res.InputStream)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    #    @unittest.skip("skipping")
    def test_put_convert_document_in_request_to_pdf(self):
        """Test case for put_convert_document_in_request_to_pdf

        :param async bool
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
        name = "putConvertToPdf.pdf"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "test1.html"
        try:

            # Upload and convert document to pdf
            self.api.put_convert_document_in_request_to_pdf(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(name)

            save_file = TestHelper.test_dst + name

            # Save to test folder
            with open(save_file, "wb") as file:
                file.write(res.InputStream)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    #    @unittest.skip("skipping")
    def test_put_convert_document_in_request_to_xps(self):
        """Test case for put_convert_document_in_request_to_xps

        :param async bool
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
        name = "putConvertToXps.xps"
        test_out_path = "HtmlTestDoc/" + name
        test_file = TestHelper.test_src + "test1.html"
        try:

            # Upload and convert document to xps
            self.api.put_convert_document_in_request_to_xps(
                out_path=test_out_path, file=test_file, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200)

            # Download result
            res = TestHelper.download_file(name)

            save_file = TestHelper.test_dst + name

            # Save to test folder
            with open(save_file, "wb") as file:
                file.write(res.InputStream)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    #    @unittest.skip("skipping")
    def test_put_convert_document_to_image(self):
        """Test case for put_convert_document_to_image

        :param async bool
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
        result_name = "putConvertDocToImg.tiff"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:

            # Convert document to image in storage
            self.api.put_convert_document_to_image(
                name, out_path=test_out_path, out_format="tiff", width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, resolution=300, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(result_name)

            save_file = TestHelper.test_dst + result_name

            # Save to test folder
            with open(save_file, "wb") as f:
                f.write(res.InputStream)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    #    @unittest.skip("skipping")
    def test_put_convert_document_to_pdf(self):
        """Test case for put_convert_document_to_pdf

        :param async bool
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
        result_name = "putConvertDocToPdf.pdf"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:

            # Convert document to pdf in storage
            self.api.put_convert_document_to_pdf(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(result_name)

            save_file = TestHelper.test_dst + result_name

            # Save to test folder
            with open(save_file, "wb") as f:
                f.write(res.InputStream)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    #    @unittest.skip("skipping")
    def test_put_convert_document_to_xps(self):
        """Test case for put_convert_document_to_xps

        :param async bool
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
        result_name = "putConvertDocToXps.xps"
        test_folder = "HtmlTestDoc"
        test_out_path = test_folder + "/" + result_name

        try:

            # Convert document to pdf in storage
            self.api.put_convert_document_to_xps(
                name, out_path=test_out_path, width=800, height=1000, left_margin=50, right_margin=100,
                top_margin=150, bottom_margin=200, folder=test_folder, storage="")

            # Download result
            res = TestHelper.download_file(result_name)

            save_file = TestHelper.test_dst + result_name

            # Save to test folder
            with open(save_file, "wb") as f:
                f.write(res.InputStream)

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


###############################################################
#                    Document test
###############################################################

    #    @unittest.skip("skipping")
    def test_get_document(self):
        """Test case for get_document

        Return the HTML document by the name from default or specified  storage.

        param async bool
        param str name: The document name. (required)
        param str storage: The document folder
        param str folder: The document folder.
        return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        name = "test_get_doc.zip"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Get document from remote storage
            res = self.api.get_document(name=name, storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get document from remote storage")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_get_document_fragment_by_x_path(self):

        """Test case for get_document_fragment_by_x_path

        Return list of HTML fragments matching the specified XPath query.

        param async bool
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
            self.assertEqual(res.Code, 200, "Error upload file to server")

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

#    @unittest.skip("skipping")
    def test_get_document_images(self):
        """Test case for get_document_images

        Return all HTML document images packaged as a ZIP archive.

        param async bool
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
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Get images from document on remote storage
            res = self.api.get_document_images(name=name, storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get images from document")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

###############################################################
#                       OCR test
###############################################################

    def test_get_recognize_and_import_to_html(self):
        """Test case for get_recognize_and_import_to_html

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
            res = self.api.get_recognize_and_import_to_html(
                file_name, ocr_engine_lang=lang, folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error OCR test")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_recognize_and_translate_to_html(self):
        """Test case for get_recognize_and_translate_to_html

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
            res = self.api.get_recognize_and_translate_to_html(file_name, src_lang, res_lang, folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error OCR and translate test")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

###############################################################
#                  Translation test
###############################################################

    def test_get_translate_document(self):
        """Test case for get_translate_document

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
            res = self.api.get_translate_document(file_name, src_lang, res_lang,
                                                              folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error translate html document")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_translate_document_by_url(self):
        """Test case for get_translate_document_by_url

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
            res = self.api.get_translate_document_by_url(source_url, src_lang, res_lang)
            self.assertTrue(isinstance(res, str), "Error translate document from url")

            # Move to test folder
            TestHelper.move_file(res, TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

###############################################################
#                  Summarization test
###############################################################

    def test_get_detect_html_keywords(self):
        """Get the HTML document keywords using the keyword detection service.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param async bool
        :param str name: Document name. (required)
        :param str folder: Document folder.
        :param str storage: Document storage.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        file_name = "test_en.html"
        try:
            # Upload file to storage
            res = TestHelper.upload_file(file_name)
            self.assertEqual(res.Code, 200, "Error upload file to server")

            # Get keywords from document
            res = self.api.get_detect_html_keywords(file_name, folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get keywords from html document")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst + 'keywordsDoc.json')
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_get_detect_html_keywords_by_url(self):
        """Get the keywords from HTML document from Web specified by its URL using the keyword detection service

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True

        :param async bool
        :param str source_url: Source document URL. (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        source_url = "https://www.le.ac.uk/oerresources/bdra/html/page_02.htm"
        try:
            # Get keyword from url
            res = self.api.get_detect_html_keywords_by_url(source_url)
            self.assertTrue(isinstance(res, str), "Error get keyword from url")

            # Move to test folder
            TestHelper.move_file(res, TestHelper.test_dst + 'keywordsUrl.json')
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
