# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="DateTime.py">
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

from storageapi.models import BaseModel


class DateTime(BaseModel):

    def __init__(self):
        """
        Attributes:
          model_types (dict): The key is attribute name and the value is attribute type.
          attribute_map (dict): The key is attribute name and the value is json key in definition.
        """
        self.model_types = {
            'Year': 'int',
            'Month': 'int',
            'Day': 'int',
            'Hour': 'int',
            'Minute': 'int',
            'Second': 'int',
            'Millisecond': 'int',
            'DayOfWeek': 'str',
            'DayOfYear': 'int',
            'Kind': 'str',
            'Ticks': 'long',
            'TimeOfDay': 'str'
        }

        self.attribute_map = {
            'Year': 'Year', 'Month': 'Month', 'Day': 'Day', 'Hour': 'Hour', 'Minute': 'Minute', 'Second': 'Second',
            'Millisecond': 'Millisecond', 'DayOfWeek': 'DayOfWeek', 'DayOfYear': 'DayOfYear', 'Kind': 'Kind',
            'Ticks': 'Ticks', 'TimeOfDay': 'TimeOfDay'}

        self.Year = None
        self.Month = None
        self.Day = None
        self.Hour = None
        self.Minute = None
        self.Second = None
        self.Millisecond = None
        self.DayOfWeek = None
        self.DayOfYear = None
        self.Kind = None
        self.Ticks = None
        self.TimeOfDay = None
