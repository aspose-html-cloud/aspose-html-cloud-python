# coding: utf-8
"""
--------------------------------------------------------------------------------------------------------------------
<copyright company="Aspose" file="conversion_result.py">
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

import pprint
import re  # noqa: F401
import six

class ConversionResult(object):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'code': 'int',
        'id': 'str',
        'status': 'str',
        'description': 'str',
        'links': 'list[str]',
        'file': 'str'
    }

    attribute_map = {
        'code': 'code',
        'id': 'id',
        'status': 'status',
        'description': 'description',
        'links': 'links',
        'file': 'file'
    }

    def __init__(self, file=None, code=None, id=None, status=None, description=None, links=None):  # noqa: E501
        self._file = None
        self.discriminator = None
        if file is not None:
            self.file = file
        self._code = None
        self._id = None
        self._status = None
        self._description = None
        self._links = None
        self.discriminator = 'Type'
        self.code = code
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links

    @property
    def code(self):
        """Gets the code of this ConversionResult.  # noqa: E501


        :return: The code of this ConversionResult.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ConversionResult.


        :param code: The code of this ConversionResult.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def id(self):
        """Gets the id of this ConversionResult.  # noqa: E501


        :return: The id of this ConversionResult.  # noqa: E501
        :rtype: Identifier
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConversionResult.


        :param id: The id of this ConversionResult.  # noqa: E501
        :type: Identifier
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this ConversionResult.  # noqa: E501


        :return: The status of this ConversionResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConversionResult.


        :param status: The status of this ConversionResult.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def description(self):
        """Gets the description of this ConversionResult.  # noqa: E501


        :return: The description of this ConversionResult.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConversionResult.


        :param description: The description of this ConversionResult.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this ConversionResult.  # noqa: E501


        :return: The links of this ConversionResult.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConversionResult.


        :param links: The links of this ConversionResult.  # noqa: E501
        :type: Links
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.model_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConversionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    @property
    def file(self):
        """Gets the file of this ConversionResult.  # noqa: E501


        :return: The file of this ConversionResult.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the files of this ConversionResult.


        :param files: The files of this ConversionResult.  # noqa: E501
        :type: str
        """

        self._file = file

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.model_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConversionResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConversionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
