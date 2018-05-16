# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_document_api.py">
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

import asposehtmlcloud
from asposehtmlcloud.api.document_api import DocumentApi
from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestDocumentApi(unittest.TestCase):

    def setUp(self):
        self.api = asposehtmlcloud.api.document_api.DocumentApi()

#    @unittest.skip("skipping")
    def test_document_get_document(self):
        """Test case for document_get_document

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
            res = self.api.document_get_document(name=name, storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get document from remote storage")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_document_get_document_fragment_by_x_path(self):

        """Test case for document_get_document_fragment_by_x_path

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
            res = self.api.document_get_document_fragment_by_x_path(name=name, x_path=x_path, out_format=out_format,
                                                                    storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get fragment document from remote storage")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

#    @unittest.skip("skipping")
    def test_document_get_document_images(self):
        """Test case for document_get_document_images

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
            res = self.api.document_get_document_images(name=name, storage="", folder=TestHelper.folder)
            self.assertTrue(isinstance(res, str), "Error get images from document")

            # Move to test folder
            TestHelper.move_file(str(res), TestHelper.test_dst)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
