# coding: utf-8

"""
    Aspose.HTML for Cloud API Reference

    OpenAPI spec version: 1.1
    
"""


from setuptools import setup, find_packages

NAME = "asposehtmlcloud"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "urllib3[secure]", "python-dateutil", "requests"]

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.HTML for Cloud API Reference",
    author_email="",
    url="",
    keywords=["Aspose.HTML for Cloud API Reference"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Aspose.HTML for Cloud API Reference
    """
)
