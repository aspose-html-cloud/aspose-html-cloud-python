# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_vectorize_api.py">
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


class TestVectorizeToSvgApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TestHelper.html
        cls.storageApi = TestHelper.storage
        cls.input_file = TestHelper.get_local_folder() + "car."

###############################################################
#           Images to SVG vectorization local to local tests
###############################################################

    def test_vectorize_local_to_local_trace_to_svg(self):
        formats = ["png", "jpg", "gif", "bmp", "tiff"]
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "SVGVectorizeLocToLoc" + ext.upper() + ".svg"
                res = self.api.vectorize_local_to_local(input_file=self.input_file + ext, output_file=output_name)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_vectorize_local_to_local_to_svg_with_opts(self):
        formats = ["png", "jpg", "gif", "bmp", "tiff"]

        opts = {
            'error_threshold': 1,
            'max_iterations': 50,
            'colors_limit': 3,
            'line_width': 1,
        }

        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "SVGVectorizeLocToLocWithOpts" + ext.upper() + ".svg"
                res = self.api.vectorize_local_to_local(input_file=self.input_file + ext, output_file=output_name,
                                                             options=opts)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex


if __name__ == '__main__':
    unittest.main()
