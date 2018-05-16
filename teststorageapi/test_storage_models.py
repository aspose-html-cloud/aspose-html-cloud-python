# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_storage_models.py">
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
import datetime
from storageapi.models import *


class TestStorageModels(unittest.TestCase):

    """Parameters
        'UsedSize': 'int',
        'TotalSize': 'int'
    """
    # @unittest.skip("skipping")
    def testDiscUsage(self):
        model1 = DiscUsage(UsedSize=100, TotalSize=200)
        model2 = DiscUsage(100, 200)
        model3 = DiscUsage(200, 300)

        self.assertTrue(isinstance(model1, DiscUsage))
        self.assertTrue(isinstance(model1.UsedSize, int))
        self.assertTrue(isinstance(model1.TotalSize, int))
        self.assertTrue(isinstance(model3.to_dict(),dict))

        dictionary = model3.to_dict()
        self.assertTrue('UsedSize' in dictionary)
        self.assertTrue('TotalSize' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'DiscUsage': 'DiscUsage'
        'Code': 'int;
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testDiscUsageResponse(self):
        d1 = DiscUsage(UsedSize=100, TotalSize=200)
        d2 = DiscUsage(100, 200)
        d3 = DiscUsage(200, 300)

        model1 = DiscUsageResponse(DiscUsage=d1, Code=200, Status='OK')
        model2 = DiscUsageResponse(d2, 200, 'OK')
        model3 = DiscUsageResponse(d3, 200, 'OK')

        self.assertTrue(isinstance(model1, DiscUsageResponse))
        self.assertTrue(isinstance(model1.DiscUsage, DiscUsage))
        self.assertTrue(isinstance(model1.DiscUsage.UsedSize,  (int, long, float)))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model3.to_dict()
        self.assertTrue('DiscUsage' in dictionary)
        self.assertTrue(model1 == model2)
        self.assertFalse(model1 == model3)

    """Parameters
        'Name': 'str',
        'IsFolder': 'bool',
        'ModifiedDate': 'datetime',
        'Size': 'int',
        'Path': 'str'
    """
    # @unittest.skip("skipping")
    def testFileDetail(self):
        model1 = FileDetail(Name='test', IsFolder=False, ModifiedDate=datetime.date.today(),
                            Size=100, Path='test_path')
        model2 = FileDetail(Name='test', IsFolder=False, ModifiedDate=datetime.date.today(),
                            Size=100, Path='test_path')
        model3 = FileDetail(Name='test', IsFolder=True, ModifiedDate=datetime.date.today(),
                            Size=0, Path='test_path',)

        self.assertTrue(isinstance(model1, FileDetail))
        self.assertTrue(isinstance(model1.Name, str))
        self.assertTrue(isinstance(model1.IsFolder, bool))
        self.assertTrue(isinstance(model1.ModifiedDate, datetime.date))
        self.assertTrue(isinstance(model1.Size, int))
        self.assertTrue(isinstance(model1.Path, str))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model3.to_dict()
        self.assertTrue('Name' in dictionary)
        self.assertTrue('IsFolder' in dictionary)
        self.assertTrue('ModifiedDate' in dictionary)
        self.assertTrue('Size' in dictionary)
        self.assertTrue('Path' in dictionary)

        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'IsExist': 'bool',
        'IsFolder': 'bool'
    """
    # @unittest.skip("skipping")
    def testFileExist(self):
        model1 = FileExist(True, True)
        model2 = FileExist(IsExist=True, IsFolder=True)
        model3 = FileExist(IsExist=True, IsFolder=False)

        self.assertTrue(isinstance(model1, FileExist))
        self.assertTrue(isinstance(model1.IsExist, bool))
        self.assertTrue(isinstance(model1.IsFolder, bool))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model3.to_dict()
        self.assertTrue('IsExist' in dictionary)
        self.assertTrue('IsFolder' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'FileExist': 'FileExist'
        'Code': 'int',
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testFileExistResponse(self):
        f1 = FileExist(True, True)
        f2 = FileExist(IsExist=True, IsFolder=True)
        f3 = FileExist(IsExist=True, IsFolder=False)

        model1 = FileExistResponse(FileExist=f1, Code=200, Status='OK')
        model2 = FileExistResponse(f2, 200, 'OK')
        model3 = FileExistResponse(f3, 200, 'OK')

        self.assertTrue(isinstance(model1, FileExistResponse))
        self.assertTrue(isinstance(model1.FileExist, FileExist))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model3.to_dict()
        self.assertTrue('FileExist' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'VersionId': 'str',
        'IsLatest': 'bool',
        'Name': 'str',
        'IsFolder': 'bool',
        'ModifiedDate': 'DateTime',
        'Size': 'long',
        'Path': 'str'
    """
    # @unittest.skip("skipping")
    def testFileVersion(self):
        model1 = FileVersion(VersionId="1.0.1", IsLatest=False, Name='test', IsFolder=False,
                             ModifiedDate=datetime.date.today(), Size=100, Path='/')
        model2 = FileVersion(VersionId="1.0.1", IsLatest=False, Name='test', IsFolder=False,
                             ModifiedDate=datetime.date.today(), Size=100, Path='/')
        model3 = FileVersion(VersionId="1.0.1", IsLatest=False, Name='test', IsFolder=True,
                             ModifiedDate=datetime.date.today(), Size=0, Path='/')

        self.assertTrue(isinstance(model1, FileVersion))
        self.assertTrue(isinstance(model1.VersionId, str))
        self.assertTrue(isinstance(model1.IsLatest, bool))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model3.to_dict()
        self.assertTrue('VersionId' in dictionary)
        self.assertTrue('IsLatest' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'FileVersions': 'list[FileVersion]',
        'Code': 'int',
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testFileVersionsResponse(self):
        v1 = FileVersion(VersionId="1.0.1", IsLatest=False)
        v2 = FileVersion(VersionId="1.0.1", IsLatest=False)
        v3 = FileVersion(VersionId="2.0.1", IsLatest=False)
        v4 = FileVersion(VersionId="3.0.1", IsLatest=True)

        model1 = FileVersionsResponse(FileVersions=[v1, v2, v3], Code=200, Status='OK')
        model2 = FileVersionsResponse(FileVersions=[v1, v2, v3], Code=200, Status='OK')
        model3 = FileVersionsResponse(FileVersions=[v1, v2, v4], Code=200, Status='OK')

        self.assertTrue(isinstance(model1, FileVersionsResponse))
        self.assertTrue(isinstance(model1.FileVersions, list))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model3.to_dict()['FileVersions'][0]
        self.assertTrue('IsLatest' in dictionary)
        self.assertTrue('VersionId' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'Code': 'int',
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testMoveFileResponse(self):
        model1 = MoveFileResponse(Code=200, Status="OK")
        model2 = MoveFileResponse(Code=200, Status="OK")
        model3 = MoveFileResponse(Code=403, Status="Forbidden")

        self.assertTrue(isinstance(model1, MoveFileResponse))
        self.assertTrue(isinstance(model1.Code, int))
        self.assertTrue(isinstance(model1.Status, str))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue('Code' in dictionary)
        self.assertTrue('Status' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'Code': 'int',
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testMoveFolderResponse(self):
        model1 = MoveFolderResponse(Code=200, Status="OK")
        model2 = MoveFolderResponse(Code=200, Status="OK")
        model3 = MoveFolderResponse(Code=403, Status="Forbidden")

        self.assertTrue(isinstance(model1, MoveFolderResponse))
        self.assertTrue(isinstance(model1.Code, int))
        self.assertTrue(isinstance(model1.Status, str))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue('Code' in dictionary)
        self.assertTrue('Status' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'Code': 'int',
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testRemoveFileResponse(self):
        model1 = RemoveFileResponse(Code=200, Status="OK")
        model2 = RemoveFileResponse(Code=200, Status="OK")
        model3 = RemoveFileResponse(Code=403, Status="Forbidden")

        self.assertTrue(isinstance(model1, RemoveFileResponse))
        self.assertTrue(isinstance(model1.Code, int))
        self.assertTrue(isinstance(model1.Status, str))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue('Code' in dictionary)
        self.assertTrue('Status' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'Code': 'int',
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testRemoveFolderResponse(self):
        model1 = RemoveFolderResponse(Code=200, Status="OK")
        model2 = RemoveFolderResponse(Code=200, Status="OK")
        model3 = RemoveFolderResponse(Code=403, Status="Forbidden")

        self.assertTrue(isinstance(model1, RemoveFolderResponse))
        self.assertTrue(isinstance(model1.Code, int))
        self.assertTrue(isinstance(model1.Status, str))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue('Code' in dictionary)
        self.assertTrue('Status' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'Code': 'int',
        'Status': 'str'
        'Message': 'str',
        'InputStream': 'str',
    """
    # @unittest.skip("skipping")
    def testResponseMessage(self):
        model1 = ResponseMessage(Code=200, Status="OK", Message='Message1', InputStream=None)
        model2 = ResponseMessage(Code=200, Status="OK", Message='Message1')
        model3 = ResponseMessage(Code=403, Status="Forbidden")

        self.assertTrue(isinstance(model1, ResponseMessage))
        self.assertTrue(isinstance(model1.Code, int))
        self.assertTrue(isinstance(model1.Status, str))
        self.assertTrue(isinstance(model1.Message, str))

        dictionary = model1.to_dict()
        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue('Code' in dictionary)
        self.assertTrue('Status' in dictionary)
        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'IsExist': 'bool',
        'Code': 'int',
        'Status': 'str'
    """
    # @unittest.skip("skipping")
    def testStorageExistResponse(self):
        model1 = StorageExistResponse(True, 200, 'OK')
        model2 = StorageExistResponse(IsExist=True, Code=200, Status='OK')
        model3 = StorageExistResponse(IsExist=False, Code=200, Status='OK')

        self.assertTrue(isinstance(model1, StorageExistResponse))
        self.assertTrue(isinstance(model1.IsExist, bool))
        self.assertTrue(isinstance(model1.Code, int))
        self.assertTrue(isinstance(model1.Status, str))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model1.to_dict()
        self.assertTrue('IsExist' in dictionary)
        self.assertTrue('Code' in dictionary)
        self.assertTrue('Status' in dictionary)

        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)


if __name__ == '__main__':
    unittest.main()
