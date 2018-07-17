# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_helper.py">
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
import os
from shutil import copy2
from asposehtmlcloud.configuration import Configuration
from storageapi.client import ApiClient as Client
from storageapi.storage_api import StorageApi


class TestHelper(object):

    # Load config from external file
    configuration = Configuration(
        apiKey="60487a72d6325241191177e37ae52146",
        appSid="80e32ca5-a828-46a4-9d54-7199dfd3764a",
        basePath="http://sikorsky-js3.dynabic.com:9083/v1.1",
        authPath="http://sikorsky-js3.dynabic.com:9083/oauth2/token",
        debug=True)

    client = Client(configuration)
    storage = StorageApi(client)
    test_src = os.path.dirname(__file__) + '/../testdata/'
    test_dst = os.path.dirname(__file__) + '/../testresult/'
    folder = 'HtmlTestDoc'

    @classmethod
    def upload_file(cls, file_name, upload_folder=None):
        folder = cls.folder if upload_folder is None else upload_folder

        response = cls.storage.PutCreate(folder + "/" + file_name, cls.test_src + file_name)
        return response

    @classmethod
    def get_file_size(cls, file_name):
        return os.path.getsize(cls.test_src + file_name)

    @classmethod
    def move_file(cls, src_file, dst_file):
        if os.path.isfile(src_file):
            copy2(src_file, dst_file)
            os.remove(src_file)

    @classmethod
    def download_file(cls, file_name, download_folder=None, save_folder=None):

        folder = cls.folder if download_folder is None else download_folder

        return cls.storage.GetDownload(folder + "/" + file_name, versionId="", storage="")