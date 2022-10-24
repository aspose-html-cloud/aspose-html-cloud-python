# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_md_api.py">
   Copyright (c) 2022 Aspose.HTML for Cloud
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

import os.path
import unittest
from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestMhtmlApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.convertApi = TestHelper.html
        cls.storageApi = TestHelper.storage
        cls.input_file = TestHelper.get_local_folder() + "fileformatinfo.mht"

###############################################################
#           MHTML conversion local to local tests
###############################################################

    def test_convert_local_to_local_mhtml_to_doc(self):
        formats = ["pdf", "xps", "docx"]
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "LocToLocMhtml." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_local_to_local_mhtml_to_doc_with_opts(self):
        formats = ["pdf", "xps", "docx"]
        options_letter = {
            'width': 8.5,
            'height': 11.0,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }
        options_A3 = {
            'width': 11.7,
            'height': 16.5,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }
        options_A4 = {
            'width': 8.3,
            'height': 11.7,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }
        options_A5 = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }

        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "testMHTML_letter." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_letter)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "testMHTML_A3." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_A3)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "testMHTML_A4." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_A4)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "testMHTML_A5." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_A5)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))

            raise ex

    def test_convert_local_to_local_mhtml_to_image(self):
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "testLocToLocMHTML." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_local_to_local_mhtml_to_image_with_opt(self):
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]
        try:
            options = {
                'width': 600,
                'height': 900,
                'topmargin': 20,
                'bottommargin': 20,
                'leftmargin': 20,
                'rightmargin': 20
            }

            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "testLocToLocMHTMLWithOpts." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

###############################################################
#           MHTML conversion local to storage tests
###############################################################

    def test_convert_local_to_storage_mhtml_to_doc(self):
        formats = ["pdf", "xps", "docx"]
        try:
            for ext in formats:
                output_name = "PythonTest/testMHTMLLocToStor." + ext
                res = self.convertApi.convert_local_to_storage(input_file=self.input_file, output_file=output_name,
                                                               storage_name=None)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                exist = self.storageApi.object_exists(res.file)
                self.assertTrue(exist.exists)
                self.assertTrue(not exist.is_folder)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_local_to_storage_mhtml_to_image(self):
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]
        try:
            for ext in formats:
                output_name = "PythonImgTest/testMHTMLLocToStor." + ext
                res = self.convertApi.convert_local_to_storage(input_file=self.input_file, output_file=output_name,
                                                               storage_name=None)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                exist = self.storageApi.object_exists(res.file)
                self.assertTrue(exist.exists)
                self.assertTrue(not exist.is_folder)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_local_to_storage_mhtml_to_image_with_opt(self):
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]

        options = {
            'width': 600,
            'height': 900,
            'topmargin': 20,
            'bottommargin': 20,
            'leftmargin': 20
        }

        try:
            for ext in formats:
                output_name = "PythonImgTestOptions/testMHTMLLocToStorWithOpts." + ext
                res = self.convertApi.convert_local_to_storage(
                    input_file=self.input_file,
                    output_file=output_name,
                    storage_name=None,
                    options=options
                )
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                exist = self.storageApi.object_exists(res.file)
                self.assertTrue(exist.exists)
                self.assertTrue(not exist.is_folder)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

###############################################################
#           MHTML conversion storage to local tests
###############################################################

    def test_convert_storage_to_local_mhtml_to_doc(self):
        file_in_storage = "PythonStorageToLocal/" + os.path.basename(self.input_file)
        res = self.storageApi.upload_file("PythonStorageToLocal", self.input_file)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        formats = ["pdf", "xps", "docx"]
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "StorToLocMHTML." + ext
                res = self.convertApi.convert_storage_to_local(input_file=file_in_storage, output_file=output_name,
                                                               storage_name=None)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_storage_to_local_mhtml_to_image(self):
        file_in_storage = "PythonStorageToLocal/" + os.path.basename(self.input_file)
        res = self.storageApi.upload_file("PythonStorageToLocal", self.input_file)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "StorToLocMHTML." + ext
                res = self.convertApi.convert_storage_to_local(input_file=file_in_storage, output_file=output_name,
                                                               storage_name=None)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_storage_to_local_mhtml_to_image_with_opt(self):
        file_in_storage = "PythonStorageToLocal/" + os.path.basename(self.input_file)
        res = self.storageApi.upload_file("PythonStorageToLocal", self.input_file)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]

        options = {
            'width': 600,
            'height': 900,
            'topmargin': 20,
            'bottommargin': 20,
            'leftmargin': 20,
            'rightmargin': 20
        }

        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "StorToLocMHTMLWithOpts." + ext
                res = self.convertApi.convert_storage_to_local(input_file=file_in_storage, output_file=output_name,
                                                               storage_name=None, options=options)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

###############################################################
#           MHTML conversion storage to storage tests
###############################################################

    def test_convert_storage_to_storage_mhtml_to_doc(self):
        file_in_storage = "PythonStorageToStorageSrc/" + os.path.basename(self.input_file)
        res = self.storageApi.upload_file("PythonStorageToStorageSrc", self.input_file)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)
        formats = ["pdf", "xps", "docx"]
        try:
            for ext in formats:
                output_name = "PythonStorageToStorageDest/StorToStorMHTML." + ext
                res = self.convertApi.convert_storage_to_storage(input_file=file_in_storage, output_file=output_name,
                                                                 storage_name=None)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                exist = self.storageApi.object_exists(res.file)
                self.assertTrue(exist.exists)
                self.assertTrue(not exist.is_folder)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_storage_to_storage_mhtml_to_image(self):
        file_in_storage = "PythonStorageToStorageSrc/" + os.path.basename(self.input_file)
        res = self.storageApi.upload_file("PythonStorageToStorageSrc", self.input_file)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]
        try:
            for ext in formats:
                output_name = "PythonStorageToStorageDest/StorToStorMHTML." + ext
                res = self.convertApi.convert_storage_to_storage(input_file=file_in_storage, output_file=output_name,
                                                                 storage_name=None)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                exist = self.storageApi.object_exists(res.file)
                self.assertTrue(exist.exists)
                self.assertTrue(not exist.is_folder)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_storage_to_storage_mhtml_to_image_with_opt(self):
        file_in_storage = "PythonStorageToStorageSrc/" + os.path.basename(self.input_file)
        res = self.storageApi.upload_file("PythonStorageToStorageSrc", self.input_file)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]

        options = {
            'width': 600,
            'height': 900,
            'topmargin': 20,
            'bottommargin': 20,
            'leftmargin': 20,
            'rightmargin': 20
        }
        try:
            for ext in formats:
                output_name = "PythonStorageToStorageDest/StorToStorMHTMLWithOpts." + ext
                res = self.convertApi.convert_storage_to_storage(input_file=file_in_storage, output_file=output_name,
                                                                 storage_name=None, options=options)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                exist = self.storageApi.object_exists(res.file)
                self.assertTrue(exist.exists)
                self.assertTrue(not exist.is_folder)
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
