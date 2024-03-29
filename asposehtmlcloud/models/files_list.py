# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
<copyright company="Aspose" file="files_list.py">
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

from asposehtmlcloud.models import BaseModel

class FilesList(BaseModel):
    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'value': 'list[StorageFile]'
    }

    attribute_map = {
        'value': 'value'
    }

    def __init__(self, value=None):

        self._value = None

        if value is not None:
            self.value = value

    @property
    def value(self):
        """Gets the value of this FilesList.

        Files and folders contained by folder StorageFile.

        :return: The value of this FilesList.
        :rtype: list[StorageFile]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FilesList.

        Files and folders contained by folder StorageFile.

        :param value: The value of this FilesList.
        :type: list[StorageFile]
        """

        self._value = value
