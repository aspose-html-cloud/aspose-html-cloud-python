# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_helper.py">
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
import os
from shutil import copy2
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.api.storage_api import StorageApi


class TestHelper(object):

    configuration = Configuration(
        basePath="https://api.aspose.cloud/v4.0",
        authPath="https://api.aspose.cloud/connect/token",
        apiKey="c8dda7d6445d82635b8797d1c8edd153",
        appSid="2225baa2-097b-4731-9831-d0d56c28230f",
        debug=True)

    client = Client(configuration)
    html = HtmlApi(client)
    storage = StorageApi(client)

    test_src = os.path.dirname(__file__) + '/../testdata/'
    test_dst = os.path.dirname(__file__) + '/../testresult/'
    folder = 'HtmlTestDoc'

    @classmethod
    def get_folder(cls):
        return cls.folder

    @classmethod
    def get_local_folder(cls):
        return cls.test_src

    @classmethod
    def get_local_dest_folder(cls):
        return cls.test_dst

    @classmethod
    def upload_file(cls, file_name):
        res = cls.storage.upload_file(cls.folder, cls.test_src + file_name)
        return res

    @classmethod
    def download_file(cls, path):
        response = cls.storage.download_file(path)
        return response

    @classmethod
    def get_file_size(cls, file_name):
        return os.path.getsize(cls.test_src + file_name)

    @classmethod
    def move_file(cls, src_file, dst_file):
        if os.path.isfile(src_file):
            copy2(src_file, dst_file)
            os.remove(src_file)
