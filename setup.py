# Modified from https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = 'pyfttt is a package for interacting with the IFTTT Maker Channel. Currently, it only supports sending events, but a lightweight web server that receives actions may be added in the future.'

setup(
    name='pyfttt',
    version='0.3',
    description='Python tools for interacting with the IFTTT Maker Channel',
    long_description=long_description,
    url='https://github.com/briandconnelly/pyfttt',
    author='Brian Connelly',
    author_email='bdc@bconnelly.net',
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
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
