# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_storage_api.py">
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
import unittest

from storageapi.storage_api import StorageApi
from teststorageapi.test_helper import TestHelper
from storageapi.client import ApiClient

class TestStorageApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TestHelper.storage

    # **************************************************
    #                  Test storage Api
    # **************************************************

    # @unittest.skip("skipping")
    def test_get_disc_usage(self):
        """Test case for get_disc_usage

        Check the disk usage of the current account
        """
        res = self.api.GetDiscUsage()
        res = res.to_dict()

        self.assertTrue('Code' in res)
        self.assertTrue('Status' in res)
        self.assertTrue('DiscUsage' in res)

        self.assertTrue(isinstance(res['Code'], int))
        self.assertTrue(isinstance(res['Status'], (str, unicode)))
        self.assertTrue(isinstance(res['DiscUsage'], dict))

        self.assertTrue('TotalSize' in res['DiscUsage'])
        self.assertTrue('UsedSize' in res['DiscUsage'])

        self.assertTrue(isinstance(res['DiscUsage']['TotalSize'], (int, float, long)))
        self.assertTrue(isinstance(res['DiscUsage']['UsedSize'], (int, float, long)))

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")
        print(res)

    # @unittest.skip("skipping")
    def test_get_is_exist(self):
        """Test case for get_is_exist

        Check if a specific file or folder exists
        """
        exist_folder = TestHelper.get_folder()

        res = self.api.GetIsExist(exist_folder)
        res = res.to_dict()

        self.assertTrue('Code' in res)
        self.assertTrue('Status' in res)
        self.assertTrue('FileExist' in res)

        self.assertTrue(isinstance(res['Code'], int))
        self.assertTrue(isinstance(res['Status'], (str, unicode)))
        self.assertTrue(isinstance(res['FileExist'], dict))

        self.assertTrue('IsFolder' in res['FileExist'])
        self.assertTrue('IsExist' in res['FileExist'])

        self.assertTrue(isinstance(res['FileExist']['IsFolder'], bool))
        self.assertTrue(isinstance(res['FileExist']['IsExist'], bool))

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        self.assertTrue(res['FileExist']['IsFolder'])
        self.assertTrue(res['FileExist']['IsExist'])
        print(res)

        non_exist_file = TestHelper.get_folder() + 'non_exist_file.gif'

        res = self.api.GetIsExist(non_exist_file)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")
        self.assertFalse(res['FileExist']['IsExist'])
        print(res)

    # @unittest.skip("skipping")
    def test_get_is_storage_exist(self):
        """Test case for get_is_storage_exist

        Check if storage exists
        """
        # {u'Status': u'OK', u'IsExist': True, u'Code': 200}
        res = self.api.GetIsStorageExist('/')
        res = res.to_dict()

        self.assertTrue('Code' in res)
        self.assertTrue('Status' in res)
        self.assertTrue('IsExist' in res)

        self.assertTrue(isinstance(res['Code'], int))
        self.assertTrue(isinstance(res['Status'], (str, unicode)))

        # ToDo IsExist receive None
        # self.assertTrue(isinstance(res['IsExist'], bool))

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        # ToDo IsExist receive None
        # self.assertTrue(res['IsExist'])
        print(res)

        res = self.api.GetIsStorageExist('/non_exist_storage/')
        res = res.to_dict()

        self.assertFalse(res['IsExist'])
        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")
        print(res)

# ToDo if name = test1.html => result test1.html, test1.html.zip
#     @unittest.skip("skipping")
    def test_get_list_file_versions(self):
        """Test case for get_list_file_versions

        Get the file's versions list
        """
        # Prepare
        file_name = "test1.html"
        src = TestHelper.get_local_folder() + file_name
        dst = TestHelper.get_folder() + file_name

        res = self.api.PutCreate(dst, src)
        res = self.api.PutCreate(dst, src)
        res = self.api.PutCreate(dst, src)

        res = self.api.GetListFileVersions(dst)
        res = res.to_dict()

        self.assertTrue('Code' in res)
        self.assertTrue('Status' in res)
        self.assertTrue('FileVersions' in res)

        self.assertTrue(isinstance(res['Code'], int))
        self.assertTrue(isinstance(res['Status'], (str, unicode)))
        self.assertTrue(isinstance(res['FileVersions'], list))

        ver = res['FileVersions'][0]
        self.assertTrue(isinstance(ver, dict))

        self.assertTrue('VersionId' in ver)
        self.assertTrue('Name' in ver)
        self.assertTrue('IsFolder' in ver)
        self.assertTrue('IsLatest' in ver)
        self.assertTrue('ModifiedDate' in ver)
        self.assertTrue('Path' in ver)
        self.assertTrue('Size' in ver)

        self.assertTrue(isinstance(ver['VersionId'], (str, unicode)))
        self.assertTrue(isinstance(ver['Name'], (str, unicode)))
        self.assertTrue(isinstance(ver['IsFolder'], bool))
        self.assertTrue(isinstance(ver['IsLatest'], bool))

        # ToDo Parse date
        self.assertTrue(isinstance(ver['ModifiedDate'], (str, unicode)))
        self.assertTrue(isinstance(ver['Path'], (str, unicode)))
        self.assertTrue(isinstance(ver['Size'], (int, long)))
        print (res)

    # **************************************************
    #                  Test file Api
    # **************************************************

    # @unittest.skip("skipping")
    def test_delete_file(self):
        """Test case for delete_file

        Remove a specific file
        """
        file_name = "test_for_delete.html"
        src = TestHelper.get_local_folder() + file_name
        dst = TestHelper.get_folder() + file_name

        res = self.api.PutCreate(dst, src)

        res = self.api.GetListFileVersions(dst)
        res = res.to_dict()
        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        print('All versions of file: ' + str(len(res['FileVersions'])))

        for item in res['FileVersions']:
            res_del = self.api.DeleteFile(dst, versionId=item['VersionId'])
            res_del = res_del.to_dict()

            self.assertEqual(res_del['Code'], 200, "Error delete file on server")
            print('File: ' + item['Name'] + ' VersionId: ' + item['VersionId'] + ' deleted on path' + item['Path'])

        res = self.api.GetIsExist(dst)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")
        self.assertFalse(res['FileExist']['IsExist'])
        print (res)

    # @unittest.skip("skipping")
    def test_get_download(self):
        """Test case for get_download

        Download a specific file
        """
        file_name = "test_en.html"
        size = TestHelper.get_file_size(file_name)

        # put file to storage
        res = TestHelper.upload_file(file_name)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200, "Error upload file to server")
        self.assertEqual(res['Status'], "OK", "Error upload file to server")

        download_file = TestHelper.get_folder() + file_name
        save_file = TestHelper.get_local_dest_folder() + file_name

        src = self.api.GetDownload(download_file)

        with open(save_file, "wb") as file:
            file.write(src.InputStream)

        self.assertTrue(os.path.getsize(save_file) == size)

    # @unittest.skip("skipping")
    def test_post_move_file(self):
        """Test case for post_move_file

        Move a specific file
        """
        file_name = "test_for_move.html"
        src = TestHelper.get_local_folder() + file_name
        remote_src = TestHelper.get_folder() + file_name

        # Put to storage
        res = self.api.PutCreate(remote_src, src)
        res = res.to_dict()
        self.assertEqual(res['Code'], 200, "Error upload file")

        remote_dst = TestHelper.get_folder() + 'test_file_moved.html'

        # Move in storage
        res = self.api.PostMoveFile(remote_src, remote_dst)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200, '')
        self.assertEqual(res['Status'].upper(), "OK", '')

        # Test dst file exist
        res = self.api.GetIsExist(remote_dst)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")
        self.assertTrue(res['FileExist']['IsExist'])
        print (res)

        # Test src file not exist
        res = self.api.GetIsExist(remote_src)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")
        self.assertFalse(res['FileExist']['IsExist'])
        print (res)

        #clear dst files
        res_del = self.api.DeleteFile(remote_dst)
        res_del = res_del.to_dict()

        self.assertEqual(res_del['Code'], 200, "Error delete file on server")
        self.assertEqual(res_del['Status'].upper(), "OK")
        print (res)

    # @unittest.skip("skipping")
    def test_put_create(self):
        """Test case for put_create

        Upload a specific file
        """
        file_name = "test_put_create.jpg"
        src = TestHelper.get_local_folder() + file_name
        dst = TestHelper.get_folder() + file_name

        self.api.PutCreate(dst, src)

        #check file exists
        res = self.api.GetIsExist(TestHelper.get_folder() + file_name)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")
        self.assertTrue(res['FileExist']['IsExist'])
        print (res)

    # **************************************************
    #                  Test folder Api
    # **************************************************

    # @unittest.skip("skipping")
    def test_put_create_folder(self):
        """Test case for put_create_folder

        Create the folder
        """
        folder_name = "test_folder"
        res = self.api.PutCreateFolder(folder_name)
        res = res.to_dict()
        self.assertEqual(res['Code'], 200, "Error create folder")
        self.assertEqual(res['Status'].upper(), "OK")

        res = self.api.GetIsExist(folder_name)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        self.assertTrue(res['FileExist']['IsFolder'])
        self.assertTrue(res['FileExist']['IsExist'])
        print(res)

    # @unittest.skip("skipping")
    def test_delete_folder(self):
        """Test case for delete_folder

        Remove a specific folder
        """
        # Create test folder
        folder_name = "tmp_folder"

        res = self.api.PutCreateFolder(folder_name)
        res = res.to_dict()
        print(res)

        self.assertEqual(res['Code'], 200, "Error create folder")
        self.assertEqual(res['Status'].upper(), "OK")

        # Delete folder
        res = self.api.DeleteFolder(folder_name)
        res = res.to_dict()
        print(res)

        self.assertEqual(res['Code'], 200, "Error delete folder")
        self.assertEqual(res['Status'].upper(), "OK")

        res = self.api.GetIsExist(folder_name)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        self.assertFalse(res['FileExist']['IsExist'])
        print(res)

    # @unittest.skip("skipping")
    def test_get_list_files(self):
        """Test case for get_list_files

        Get the file listing of a specific folder
        """
        res = self.api.GetListFiles()
        res = res.to_dict()

        self.assertTrue('Code' in res)
        self.assertTrue('Status' in res)
        self.assertTrue('Files' in res)

        self.assertEqual(res['Code'], 200, "Error get list of files")
        self.assertEqual(res['Status'].upper(), "OK", "Error get list of files")

        file_list = res['Files']
        self.assertTrue(isinstance(file_list, list))

        one_file = file_list[0]
        self.assertTrue(isinstance(one_file, dict))

        self.assertTrue('IsFolder' in one_file)
        self.assertTrue('IsFolder' in one_file)
        # ToDo ModifiedDate IS STRING -  '/Date(-62135596800000)/'
        self.assertTrue('ModifiedDate' in one_file)
        self.assertTrue('Name' in one_file)
        self.assertTrue('Path' in one_file)
        self.assertTrue('Size' in one_file)

        self.assertTrue(isinstance(one_file['IsFolder'], bool))
        self.assertTrue(isinstance(one_file['ModifiedDate'], (str, unicode)))
        self.assertTrue(isinstance(one_file['Name'], (str, unicode)))
        self.assertTrue(isinstance(one_file['Path'], (str, unicode)))
        self.assertTrue(isinstance(one_file['Size'], (int, long)))

        for f in file_list:
            print (f)

    # @unittest.skip("skipping")
    def test_post_move_folder(self):
        """Test case for post_move_folder

        Move a specific folder
        """
        old_folder = "test_move_folder"

        # Prepare test, create folder
        res = self.api.PutCreateFolder(old_folder)
        res = res.to_dict()
        print(res)

        self.assertEqual(res['Code'], 200, "Error create folder")
        self.assertEqual(res['Status'].upper(), "OK")

        new_folder = 'test_dest_folder'

        # Move folder
        res = self.api.PostMoveFolder(old_folder, new_folder)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200, "Error move folder")
        self.assertEqual(res['Status'].upper(), "OK")

        # Check new folder exist
        res = self.api.GetIsExist(new_folder)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        self.assertTrue(res['FileExist']['IsFolder'], 'After move new folder not exist')
        self.assertTrue(res['FileExist']['IsExist'], 'After move new folder not exist')
        print(res)

        # Check not exists old folder
        res = self.api.GetIsExist(old_folder)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        self.assertFalse(res['FileExist']['IsExist'], 'After move olf folder exist')
        print(res)

        # Delete new folder (cleanup)
        res = self.api.DeleteFolder(new_folder)
        res = res.to_dict()
        print(res)

        self.assertEqual(res['Code'], 200, "Error delete folder")
        self.assertEqual(res['Status'].upper(), "OK")

        res = self.api.GetIsExist(new_folder)
        res = res.to_dict()

        self.assertEqual(res['Code'], 200)
        self.assertEqual(res['Status'].upper(), "OK")

        self.assertFalse(res['FileExist']['IsExist'])
        print(res)


if __name__ == '__main__':
    unittest.main()
