# Modified from https://github.com/pypa/sampleproject/blob/master/setup.py

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

import pyfttt

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
#with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
#    long_description = f.read()

long_description = 'A AM A LONG DESCRIPTION'

setup(
    name='pyfttt',
    version=pyfttt.__version__,
    description='Python tools for interacting with the IFTTT Maker Channel',
    long_description=long_description,
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
    ],

    # What does your project relate to?
    keywords='IFTTT automation',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['requests'],

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
