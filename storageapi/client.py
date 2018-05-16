# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="client.py">
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

import datetime
import json
import mimetypes
import urllib
import urllib2
import logging
import re
import requests

# python 2 and python 3 compatibility library
import six
from storageapi.models import *

class ApiClient(object):
    """Generic API client for client library builds.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to the API.
    :param cookie: a cookie to include in the header when making calls to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self, configuration, header_name=None, header_value=None, cookie=None):

        self.configuration = configuration
        self.default_headers = {}
        self.boundary = 'Somthing'

        #setup OAuth2
        self.default_headers['Authorization'] = configuration.access_token

        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = configuration.default_user_agent

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    @staticmethod
    def build_uri(path, qry_data=None):
        """
        URI Builder - Accept path and query string to generate a URI.

        :param path: e.g http://api-qa.aspose.com/v1/testurl
        :param qry_data: a dictionary which holds query string data e.g {'param1': 'value1', 'param2': 'value2'}
        :return: returns a uri with query string e.g http://api-qa.aspose.com/v1/testurl?param1=value1&param2=value2
        """

        del_dict = {}

        if 'file' in qry_data:
            del qry_data['file']

        for (key, val) in qry_data.iteritems():
            if (path.find('{' + key.lower() + '}') >= 0):
                path = path.replace('{' + key.lower() + '}', val)
                del_dict[key] = val

        for (key, val) in del_dict.iteritems():
            del qry_data[key]

        path = path.rstrip('/')

        if qry_data:
            return path + '?' + urllib.urlencode(qry_data)
        else:
            return path

    def call_api(self, resource_path, method, query_params, post_data, header_params=None, files=None):

        resource_path = re.sub("\\{\\w*\\}", "", resource_path)

        url = self.configuration.config['basePath'] + resource_path
        logging.debug(url)

        mergedHeaderParams = self.default_headers.copy()
        mergedHeaderParams.update(header_params)
        headers = {}
        if mergedHeaderParams:
            for param, value in mergedHeaderParams.iteritems():
                headers[param] = ApiClient.sanitizeForSerialization(value)

        if self.cookie:
            headers['Cookie'] = ApiClient.sanitizeForSerialization(self.cookie)

        data = None

        if method in ['GET']:
            #Options to add statements later on and for compatibility
            pass

        elif method in ['POST', 'PUT', 'DELETE']:
            if post_data:
                post_data = ApiClient.sanitizeForSerialization(post_data)
                if 'Content-type' not in headers:
                    headers['Content-type'] = 'application/json'
                    data = json.dumps(post_data)
                elif headers['Content-type'] == 'multipart/form-data':
                    data = self.buildMultipartFormData(post_data, files)

                    headers['Content-type'] = 'multipart/form-data; boundary={0}'.format(self.boundary)
                    headers['Content-length'] = str(len(data))
                else:
                    data = urllib.urlencode(post_data)
            elif files:
                headers['Content-type'] = 'multipart/form-data; boundary={0}'.format(self.boundary)
        else:
            raise Exception('Method ' + method + ' is not recognized.')

        if headers['Accept'].find('application/octet-stream') or files:
            stream = True
        else:
            stream = False

        if method == 'GET':
                response = requests.get(url, headers=headers, stream=stream, files=files)
        elif method == 'PUT':
            if 'file' in files and files['file'] and len(files) == 1:
                response = requests.put(url, files['file'], headers=headers, stream=stream)
            else:
                response = requests.put(url,data,headers=headers, stream=stream, files=files)
        elif method == 'POST':
            if 'file' in files and files['file'] and len(files) == 1:
                response = requests.post(url, files['file'], headers=headers, stream=stream)
            else:
                response = requests.post(url, data, headers=headers, stream=stream, files=files)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, stream=stream, files=files)

        return response

    def toPathValue(self, obj):
        """Convert a string or object to a path-friendly value
        Args:
        :param obj obj: Object or string value
        :return: string -- quoted value
        """
        if type(obj) == list:
            return ','.join(obj)
        else:
            return str(obj)

    @staticmethod
    def sanitizeForSerialization(obj):
        """
        Sanitize an object for Request.
        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date convert to string in iso8601 format.
        If obj is list, santize each element in the list.
        If obj is dict, return the dict.
        If obj is model, return the properties dict.
        """
        if isinstance(obj, type(None)):
            return None
        elif isinstance(obj, (str, unicode, int, long, float, bool, file)):
            return obj
        elif isinstance(obj, list):
            return [ApiClient.sanitizeForSerialization(subObj) for subObj in obj]
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            if isinstance(obj, dict):
                objDict = obj
            else:
                # Convert model obj to dict except attributes `model_types`, `attribute_map`
                # and attributes which value is not None.
                # Convert attribute name to json key in model definition for request.
                objDict = {obj.attribute_map[key]: val
                           for key, val in obj.__dict__.iteritems()
                           if key != 'model_types' and key != 'attribute_map' and val is not None}
            return {key: ApiClient.sanitizeForSerialization(val)
                    for (key, val) in objDict.iteritems()}

    def buildMultipartFormData(self, post_data, files):
        def escape_quotes(s):
            return s.replace('"', '\\"')

        lines = []

        for name, value in post_data.items():
            lines.extend((
                '--{0}'.format(self.boundary),
                'Content-Disposition: form-data; name="{0}"'.format(escape_quotes(name)),
                '',
                str(value),
            ))

        for name, filepath in files.items():
            f = open(filepath, 'r')
            filename = filepath.split('/')[-1]
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
            lines.extend((
                '--{0}'.format(self.boundary),
                'Content-Disposition: form-data; name="{0}"; filename="{1}"'.format(escape_quotes(name),
                                                                                    escape_quotes(filename)),
                'Content-Type: {0}'.format(mimetype),
                '',
                f.read()
            ))

        lines.extend((
            '--{0}--'.format(self.boundary),
            ''
        ))
        return '\r\n'.join(lines)

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

        :param obj: String or object to be deserialized
        :param objClass: Class literal for deserialzied object, or string of class name

        :return: bject -- deserialized object
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


class MethodRequest(urllib2.Request):
    def __init__(self, *args, **kwargs):
        """Construct a MethodRequest. Usage is the same as for
        `urllib2.Request` except it also takes an optional `method`
        keyword argument. If supplied, `method` will be used instead of
        the default.
        """

        if 'method' in kwargs:
            self.method = kwargs.pop('method')
        urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self):
        return getattr(self, 'method', urllib2.Request.get_method(self))
