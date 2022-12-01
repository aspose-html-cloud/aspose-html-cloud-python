# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_svg_api.py">
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


class TestSvgApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.convertApi = TestHelper.html
        cls.storageApi = TestHelper.storage
        cls.input_file = TestHelper.get_local_folder() + "Map-World.svg"

###############################################################
#           SVG conversion local to local tests
###############################################################

    def test_convert_local_to_local_svg_to_doc(self):
        formats = ["pdf", "xps"]
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "SVGLocToLoc." + ext
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

    def test_convert_local_to_local_svg_to_doc_with_opts(self):
        formats = ["pdf", "xps"]
        options_letter = {
            'width': 8.5,
            'height': 11.0,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }
        options_a3 = {
            'width': 11.7,
            'height': 16.5,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }
        options_a4 = {
            'width': 8.3,
            'height': 11.7,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }
        options_a5 = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5
        }
        options_a5_red = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5,
            'background': '#FF0000'
        }
        options_a5_green = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5,
            'background': '#00FF00'
        }
        options_a5_blue = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5,
            'background': '#0000FF'
        }
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "svg_letter." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_letter)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A3." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a3)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A4." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a4)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A5." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a5)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A5_red." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a5_red)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A5_green." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a5_green)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A5_blue." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a5_blue)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))

            raise ex

    def test_convert_local_to_local_svg_to_doc_with_opts_background(self):
        formats = ["pdf", "xps"]
        options_a5_red = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5,
            'background': '#FF0000'
        }
        options_a5_green = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5,
            'background': '#00FF00'
        }
        options_a5_blue = {
            'width': 5.8,
            'height': 8.3,
            'topmargin': 0.5,
            'bottommargin': 0.5,
            'leftmargin': 0.5,
            'rightmargin': 0.5,
            'background': '#0000FF'
        }
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "svg_A5_red." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a5_red)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A5_green." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a5_green)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

                output_name = TestHelper.get_local_dest_folder() + "svg_A5_blue." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name,
                                                             options=options_a5_blue)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(res.status == 'completed')
                self.assertTrue(os.path.exists(res.file))

        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))

            raise ex

    def test_convert_local_to_local_svg_to_image(self):
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]
        try:
            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "SVGToImg." + ext
                res = self.convertApi.convert_local_to_local(input_file=self.input_file, output_file=output_name)
                self.assertTrue(isinstance(res.id, str), "Error create task")
                self.assertTrue(isinstance(res.code, int), "Error get task's id")
                self.assertTrue(res.code == 200, "Error code for create task")
                self.assertTrue(os.path.exists(res.file))
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_convert_local_to_local_svg_to_image_with_opt(self):
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
                output_name = TestHelper.get_local_dest_folder() + "SVGToImg600x900x20x20x20x20." + ext
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

    def test_convert_local_to_local_svg_to_image_with_opt_background(self):
        formats = ["jpeg", "jpg", "bmp", "png", "tiff", "tif", "gif"]
        try:
            options = {
                'width': 800,
                'height': 1200,
                'topmargin': 20,
                'bottommargin': 20,
                'leftmargin': 20,
                'rightmargin': 20,
                'background': '#00FF00'
            }

            for ext in formats:
                output_name = TestHelper.get_local_dest_folder() + "SVGToImg800x1200x20x20x20x20_green." + ext
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


if __name__ == '__main__':
    unittest.main()
