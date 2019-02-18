# coding: utf-8

from setuptools import setup, find_packages

NAME = "asposehtmlcloud"
VERSION = "1.0.8"
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
    description='Aspose.HTML for Cloud API Reference',
    author='Aspose',
    author_email='alexander.makogon@aspose.com',
    url="https://products.aspose.cloud/html",
    license='MIT',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=["Aspose.HTML for Cloud API Reference", "Aspose", "Html cloud"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Aspose.HTML for Cloud API Reference
    """
)
