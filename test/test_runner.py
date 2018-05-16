# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_runner.py">
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

import unittest
from test.test_conversion_api import TestConversionApi
from test.test_document_api import TestDocumentApi
from test.test_ocr_api import TestOcrApi
from test.test_translation_api import TestTranslationApi


all_test = unittest.TestSuite()
all_test.addTest(unittest.makeSuite(TestConversionApi))
all_test.addTest(unittest.makeSuite(TestDocumentApi))
all_test.addTest(unittest.makeSuite(TestOcrApi))
all_test.addTest(unittest.makeSuite(TestTranslationApi))

print("count of tests: " + str(all_test.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(all_test)
