#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

this_dir = os.path.dirname(__file__)
long_description = open(os.path.join(this_dir, 'README.rst')).read()

# Hack stuff that is useful for GitHub but not understood by PyPI :-(
long_description = long_description.replace('Example usage:\n\n.. code:: python', 'Example usage::')

setup(
    name='djangotestxmlrpc',
    version='0.0.1',
    description="""Utility classes for testing Django views that speak XML-RPC""",
    long_description=long_description,
    keywords='unittest,testing,Django,XML-RPC',
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    url='https://github.com/msabramo/djangotestxmlrpc',
    py_modules=['djangotestxmlrpc'],
    test_suite='tests',
    tests_require=['mock', 'six'],
    use_2to3=True,
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ]
)
