#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script for installing pyfttt.

To install, run:

    python setup.py install

"""

# Modified from https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages

from codecs import open
from os import path
import sys


if sys.argv[-1] == 'setup.py':
    print("To install pyfttt, run 'python setup.py install'\n")

if sys.version_info[:2] < (2, 7):
    print("pyfttt requires Python 2.7 or later (%d.%d detected)." % sys.version_info[:2])
    sys.exit(-1)


here = path.abspath(path.dirname(__file__))


setup(
    name='pyfttt',
    version='0.3.2',
    description='Python tools for interacting with the IFTTT Webhooks Channel',
    long_description='pyfttt is a lightweight package for sending events to the IFTTT Webhooks Channel. Currently, it only supports sending events, but future releases may include a webserver for receiving events.',
    url='https://github.com/briandconnelly/pyfttt',
    author='Brian Connelly',
    author_email='bdc@bconnelly.net',
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='IFTTT automation',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['requests>=2.7'],

    extras_require={},
    package_data={},
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pyfttt=pyfttt.cmd_script:main',
        ],
    },
)

