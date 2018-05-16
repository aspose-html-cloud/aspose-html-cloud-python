# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="storage_api.py">
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

import json
import re


class StorageApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def DeleteFile(self, Path, **kwargs):
        """Remove a specific file. Parameters: path - file path e.g. /file.ext,
        versionID - file's version, storage - user's storage name.

        :param str Path: File path e.g. /file.ext. (required)
        :param str versionId: File version. (optional)
        :param str storage: Remote storage. (optional)

        :return: RemoveFileResponse
        """

        all_params = dict.fromkeys(['Path', 'versionId', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteFile" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/file/{path}/?versionId={versionId}&amp;storage={storage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}", str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'versionId' in all_params and all_params['versionId'] is not None:
            res_path = res_path.replace("{" + "versionId" + "}", str(all_params['versionId']))
        else:
            res_path = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        method = 'DELETE'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'RemoveFileResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def GetDiscUsage(self, **kwargs):
        """Check the disk usage of the current account.
        Parameters: storage - user's storage name.

        :param str storage: Remote storage. (optional)

        :return: DiscUsageResponse
        """

        all_params = dict.fromkeys(['storage'])

        for (key, val) in kwargs.iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetDiscUsage" % key)
            all_params[key] = val

        res_path = '/storage/disc/?storage={storage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        method = 'GET'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)

        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'DiscUsageResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def GetDownload(self, Path, **kwargs):
        """Download a specific file.
        Parameters: path - file path e.g. /file.ext, versionID - file's version,
        storage - user's storage name.

        :param str Path: File path e.g. /file.ext. (required)
        :param str versionId:  File version (optional)
        :param str storage: Remote storage. (optional)

        :return: ResponseMessage
        """

        all_params = dict.fromkeys(['Path', 'versionId', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetDownload" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/file/{path}/?versionId={versionId}&amp;storage={storage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}", str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)
        
        if 'versionId' in all_params and all_params['versionId'] is not None:
            res_path = res_path.replace("{" + "versionId" + "}", str(all_params['versionId']))
        else:
            res_path = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        method = 'GET'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/octet-stream'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'ResponseMessage',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def GetIsExist(self, Path, **kwargs):
        """Check if a specific file or folder exists.
        Parameters: path - ,
        versionID - file's version,
        storage - user's storage name.
        :param str Path: File path e.g. /file.ext. (required)
        :param versionId (str):  (optional)
        :param str Path: File or folder path e.g. /file.ext or /Folder1
        :param str storage: Remote storage. (optional)

        :return: FileExistResponse
        """

        all_params = dict.fromkeys(['Path', 'versionId', 'storage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetIsExist" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/exist/{path}/?versionId={versionId}&amp;storage={storage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}", str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'versionId' in all_params and all_params['versionId'] is not None:
            res_path = res_path.replace("{" + "versionId" + "}", str(all_params['versionId']))
        else:
            res_path = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        method = 'GET'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'
        post_data = (form_params if form_params else body_param)

        response = self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'FileExistResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def GetListFileVersions(self, Path, **kwargs):
        """Get the file's versions list.
        Parameters: path - file path e.g. /file.ext or /Folder1/file.ext,
        storage - user's storage name.

        :param str Path: File path e.g. /file.ext. (required)
        :param str storage: Remote storage. (optional)

        :return: FileVersionsResponse
        """

        all_params = dict.fromkeys(['Path', 'storage'])
        all_params['Path'] = Path

        for (key, val) in kwargs.iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetListFileVersions" % key)
            all_params[key] = val
        
        res_path = '/storage/version/{path}/?storage={storage}'
        res_path = res_path.replace('&amp;', '&').replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}", str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        method = 'GET'
        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response = self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'FileVersionsResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def PostMoveFile(self, src, dest, **kwargs):
        """Move a specific file.

        :param str src: Source file path e.g. /file.ext (required)
        :param str dest: Destination (required)
        :param str versionId: Source file's version, (optional)
        :param str storage: Remote storage. (optional)
        :param str destStorage: User's destination storage name (optional)

        :return: MoveFileResponse
        """

        all_params = dict.fromkeys(['src', 'dest', 'versionId', 'storage', 'destStorage'])

        all_params['src'] = src
        all_params['dest'] = dest

        for (key, val) in kwargs.iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method PostMoveFile" % key)
            all_params[key] = val

        res_path = '/storage/file/{src}/?dest={dest}&amp;versionId={versionId}&amp;storage={storage}' \
                   '&amp;destStorage={destStorage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'src' in all_params and all_params['src'] is not None:
            res_path = res_path.replace("{" + "src" + "}", str(all_params['src']))
        else:
            res_path = re.sub("[&?]src.*?(?=&|\\?|$)", "", res_path)

        if 'dest' in all_params and all_params['dest'] is not None:
            res_path = res_path.replace("{" + "dest" + "}", str(all_params['dest']))
        else:
            res_path = re.sub("[&?]dest.*?(?=&|\\?|$)", "", res_path)

        if 'versionId' in all_params and all_params['versionId'] is not None:
            res_path = res_path.replace("{" + "versionId" + "}", str(all_params['versionId']))
        else:
            res_path = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        if 'destStorage' in all_params and all_params['destStorage'] is not None:
            res_path = res_path.replace("{" + "destStorage" + "}", str(all_params['destStorage']))
        else:
            res_path = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", res_path)

        method = 'POST'
        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'MoveFileResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def PutCopy(self, Path, newdest, file, **kwargs):
        """Copy a specific file.
        Parameters: path - source file path e.g. /file.ext,
        versionID - source file's version,
        storage - user's source storage name,
        newdest - destination file path, destStorage - user's destination storage name.

        :param str Path: File path e.g. /file.ext. (required)
        :param str newdest:  New file path (required)
        :param str versionId:  File version(optional)
        :param str storage: Remote storage. (optional)

        :param str destStorage:  (optional)
        :param str file:  File path e.g. /file.ext (required)

        :return: ResponseMessage
        """

        all_params = dict.fromkeys(['Path', 'newdest', 'versionId', 'storage', 'destStorage', 'file'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method PutCopy" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/file/{path}/?newdest={newdest}&amp;versionId={versionId}&amp;storage={storage}' \
                   '&amp;destStorage={destStorage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}", str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'newdest' in all_params and all_params['newdest'] is not None:
            res_path = res_path.replace("{" + "newdest" + "}", str(all_params['newdest']))
        else:
            res_path = re.sub("[&?]newdest.*?(?=&|\\?|$)", "", res_path)

        if 'versionId' in all_params and all_params['versionId'] is not None:
            res_path = res_path.replace("{" + "versionId" + "}", str(all_params['versionId']))
        else:
            res_path = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        if 'destStorage' in all_params and all_params['destStorage'] is not None:
            res_path = res_path.replace("{" + "destStorage" + "}", str(all_params['destStorage']))
        else:
            res_path = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", res_path)

        method = 'PUT'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { 'file':open(file, 'rb')}
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'multipart/form-data'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'ResponseMessage',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def PutCreate(self, Path, file, **kwargs):
        """Upload a specific file.
        Parameters: path - source file path e.g. /file.ext,
        versionID - source file's version,
        storage - user's source storage name,
        newdest - destination file path,
        destStorage - user's destination storage name.

        :param str Path: Remote file path e.g. /file.ext. (required)
        :param str versionId:  (optional)
        :param str storage: Remote storage. (optional)
        :param str file:  Local File name with full path (required)

        :return: ResponseMessage
        """

        all_params = dict.fromkeys(['Path', 'versionId', 'storage', 'file'])
        all_params['Path'] = Path
        all_params['file'] = file

        for (key, val) in kwargs.iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method PutCreate" % key)
            all_params[key] = val
        
        res_path = '/storage/file/{path}/?versionId={versionId}&amp;storage={storage}'
        res_path = res_path.replace('&amp;','&')\
            .replace("/?","?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}", str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'versionId' in all_params and all_params['versionId'] is not None:
            res_path = res_path.replace("{" + "versionId" + "}", str(all_params['versionId']))
        else:
            res_path = re.sub("[&?]versionId.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        method = 'PUT'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { 'file':open(file, 'rb')}
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'multipart/form-data'

        post_data = (form_params if form_params else body_param)
        response = self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'ResponseMessage',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code, response.content)
        except Exception:
            raise ApiException(response.status_code, response.content)

    def DeleteFolder(self, Path, **kwargs):
        """Remove a specific folder.
        Parameters: path - folder path e.g. /Folder1, storage - user's storage name,
        recursive - is subfolders and files must be deleted for specified path.

        :param str Path: File path e.g. /file.ext. (required)
        :param str storage: Remote storage. (optional)
        :param bool recursive:  Delete recursive (optional)

        :return: RemoveFolderResponse
        """

        all_params = dict.fromkeys(['Path', 'storage', 'recursive'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/folder/{path}/?storage={storage}&amp;recursive={recursive}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}", str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}", str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        if 'recursive' in all_params and all_params['recursive'] is not None:
            res_path = res_path.replace("{" + "recursive" + "}", str(all_params['recursive']))
        else:
            res_path = re.sub("[&?]recursive.*?(?=&|\\?|$)", "", res_path)

        method = 'DELETE'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'RemoveFolderResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def GetListFiles(self, **kwargs):
        """Get the file listing of a specific folder.
        Parametres: path - start with name of storage e.g. root folder '/'or some folder '/folder1/..',
        storage - user's storage name.

        :param str Path: File path e.g. /file.ext. (required)
        :param str storage: Remote storage. (optional)

        :return: FilesResponse
        """

        all_params = dict.fromkeys(['Path', 'storage'])

        for (key, val) in kwargs.iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetListFiles" % key)
            all_params[key] = val
        
        res_path = '/storage/folder/{path}/?storage={storage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}" , str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}" , str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        method = 'GET'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response = self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'FilesResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def PostMoveFolder(self, src, dest, **kwargs):
        """Move a specific folder. Parameters: src - source folder path e.g. /Folder1,
        storage - user's source storage name,
        dest - destination folder path e.g. /Folder2,
        destStorage - user's destination storage name.

        :param str src: Source folder (required)
        :param str dest: Target folder (required)
        :param str storage: Remote storage. (optional)
        :param str destStorage: Storage (optional)

        :return: MoveFolderResponse
        """

        all_params = dict.fromkeys(['src', 'dest', 'storage', 'destStorage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method PostMoveFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/folder/{src}/?dest={dest}&amp;storage={storage}&amp;destStorage={destStorage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'src' in all_params and all_params['src'] is not None:
            res_path = res_path.replace("{" + "src" + "}" , str(all_params['src']))
        else:
            res_path = re.sub("[&?]src.*?(?=&|\\?|$)", "", res_path)

        if 'dest' in all_params and all_params['dest'] is not None:
            res_path = res_path.replace("{" + "dest" + "}" , str(all_params['dest']))
        else:
            res_path = re.sub("[&?]dest.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}" , str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        if 'destStorage' in all_params and all_params['destStorage'] is not None:
            res_path = res_path.replace("{" + "destStorage" + "}" , str(all_params['destStorage']))
        else:
            res_path = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", res_path)

        method = 'POST'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'MoveFolderResponse', response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def PutCopyFolder(self, Path, newdest, **kwargs):
        """Copy a folder. Parameters: path - source folder path e.g. /Folder1,
        storage - user's source storage name, newdest - destination folder path e.g. /Folder2,
        destStorage - user's destination storage name.

        :param str Path: File path e.g. /file.ext. (required)
        :param str newdest:  (required)
        :param str storage: Remote storage. (optional)
        :param str destStorage:  (optional)

        :return: ResponseMessage
        """

        all_params = dict.fromkeys(['Path', 'newdest', 'storage', 'destStorage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method PutCopyFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/folder/{path}/?newdest={newdest}&amp;storage={storage}&amp;destStorage={destStorage}'
        res_path = res_path.replace('&amp;','&').replace("/?","?").replace("toFormat={toFormat}","format={format}").replace("{path}","{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}" , str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'newdest' in all_params and all_params['newdest'] is not None:
            res_path = res_path.replace("{" + "newdest" + "}" , str(all_params['newdest']))
        else:
            res_path = re.sub("[&?]newdest.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}" , str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        if 'destStorage' in all_params and all_params['destStorage'] is not None:
            res_path = res_path.replace("{" + "destStorage" + "}" , str(all_params['destStorage']))
        else:
            res_path = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", res_path)

        method = 'PUT'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'ResponseMessage', response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def PutCreateFolder(self, Path, **kwargs):
        """Create the folder. Parameters: path - source folder path e.g.
        /Folder1, storage - user's source storage name,
        newdest - destination folder path e.g. /Folder2,
        destStorage - user's destination storage name.

        :param str Path: File path e.g. /file.ext. (required)
        :param str storage: Remote storage. (optional)
        :param str destStorage:  (optional)

        :return: ResponseMessage
        """

        all_params = dict.fromkeys(['Path', 'storage', 'destStorage'])

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method PutCreateFolder" % key)
            params[key] = val
        
        for (key, val) in params.iteritems():
            if key in all_params:
                all_params[key] = val
        
        res_path = '/storage/folder/{path}/?storage={storage}&amp;destStorage={destStorage}'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'Path' in all_params and all_params['Path'] is not None:
            res_path = res_path.replace("{" + "Path" + "}" , str(all_params['Path']))
        else:
            res_path = re.sub("[&?]Path.*?(?=&|\\?|$)", "", res_path)

        if 'storage' in all_params and all_params['storage'] is not None:
            res_path = res_path.replace("{" + "storage" + "}" , str(all_params['storage']))
        else:
            res_path = re.sub("[&?]storage.*?(?=&|\\?|$)", "", res_path)

        if 'destStorage' in all_params and all_params['destStorage'] is not None:
            res_path = res_path.replace("{" + "destStorage" + "}" , str(all_params['destStorage']))
        else:
            res_path = re.sub("[&?]destStorage.*?(?=&|\\?|$)", "", res_path)

        method = 'PUT'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response =  self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'ResponseMessage', response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def GetIsStorageExist(self, name, **kwargs):
        """Check if a specific storage exists.

        :param str storage: Storage name (required)

        :return: StorageExistResponse
        """

        all_params = dict.fromkeys(['name'])
        all_params['name'] = name

        params = locals()
        for (key, val) in kwargs.iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetIsStorageExist" % key)
                all_params[key] = val
        
        res_path = '/storage/{name}/exist/?'
        res_path = res_path.replace('&amp;', '&')\
            .replace("/?", "?")\
            .replace("toFormat={toFormat}", "format={format}")\
            .replace("{path}", "{Path}")

        if 'name' in all_params and all_params['name'] is not None:
            res_path = res_path.replace("{" + "name" + "}" , str(all_params['name']))
        else:
            res_path = re.sub("[&?]name.*?(?=&|\\?|$)", "", res_path)

        method = 'GET'
        query_params = {}
        header_params = {}
        form_params = {}
        files = { }
        body_param = None

        header_params['Accept'] = 'application/xml,application/json'
        header_params['Content-Type'] = 'application/json'

        post_data = (form_params if form_params else body_param)
        response = self.api_client.call_api(res_path, method, query_params, post_data, header_params, files=files)

        try:
            if response.status_code in [200,201,202]:
                res_obj = self.api_client.pre_deserialize(response.content, 'StorageExistResponse',
                                                          response.headers['content-type'])
                return res_obj
            else:
                raise ApiException(response.status_code,response.content)
        except Exception:
            raise ApiException(response.status_code,response.content)

    def pre_deserialize(self, obj, objClass, contentType=None):

        if objClass == 'ResponseMessage':
            if contentType is not None and "application/json" not in contentType:
                objClass = eval('ResponseMessage')
                objClass.Status = 'OK'
                objClass.Code = 200
                objClass.InputStream = obj
                return objClass

        if contentType is None or "application/json" not in contentType:
            raise ApiException(406, "Invalid contentType " + str(contentType))

        jsonObj = json.loads(obj)
        logging.debug("JSON Body :: " + str(jsonObj))
        return self.deserialize(jsonObj, objClass)

    def deserialize(self, obj, objClass):
        """Derialize a JSON string into an object.
        :param obj obj: String or object to be deserialized
        :param str objClass: Class literal for deserialzied object, or string of class name
        :return: object -- deserialized object
        """

        # Have to accept objClass as string or actual type. Type could be a
        # native Python type, or one of the model classes.
        if obj is None:
            return

        if type(objClass) == str:
            if 'list[' in objClass:
                match = re.match('list\[(.*)\]', objClass)
                subClass = match.group(1)
                if obj is not None:
                    return [self.deserialize(subObj, subClass) for subObj in obj]
                else:
                    return;

            objClass = eval(objClass)

        if objClass in [int, long, float, dict, list, str, bool]:
            return objClass(obj)
        elif objClass == datetime:
            return self.__parse_string_to_datetime(obj)

        instance = objClass()

        for attr, attrType in instance.model_types.iteritems():
            logging.debug(attr + ',' + attrType)
            if obj is not None and instance.attribute_map[attr] in obj and type(obj) in [list, dict]:
                value = obj[instance.attribute_map[attr]]
                if attrType in ['str', 'int', 'long', 'float', 'bool']:
                    attrType = eval(attrType)
                    try:
                        value = attrType(value)
                    except UnicodeEncodeError:
                        value = unicode(value)
                    except TypeError:
                        value = value
                    setattr(instance, attr, value)
                elif (attrType == 'datetime'):
                    setattr(instance, attr, self.__parse_string_to_datetime(value))
                else:
                    setattr(instance, attr, self.deserialize(value, attrType))
            elif obj is not None and instance.attribute_map[attr] not in obj:
                continue
            elif 'list[' in attrType:
                match = re.match('list\[(.*)\]', attrType)
                subClass = match.group(1)
                subValues = []
                if not value:
                    setattr(instance, attr, None)
                else:
                    for subValue in value:
                        subValues.append(self.deserialize(subValue, subClass))
                setattr(instance, attr, subValues)
            else:
                value = obj[instance.attribute_map[attr]]
                setattr(instance, attr, self.deserialize(value, attrType))

        return instance

    def __parse_string_to_datetime(self, string):
        """
        Parse datetime in string to datetime.
        The string should be in iso8601 datetime format.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string


class ApiException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def set_code(self, code):
        self.code = code

    def set_message(self, message):
        self.message = message
