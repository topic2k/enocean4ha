#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='enocean',
    version='0.60.1',
    description='EnOcean serial protocol implementation',
    author='Kimmo Huoman',
    author_email='kipenroskaposti@gmail.com',
    url='https://github.com/kipe/enocean',
    packages=[
        'enocean',
        'enocean.protocol',
        'enocean.communicators',
    ],
    scripts=[
        'examples/enocean_example.py',
    ],
    package_data={
        '': ['EEP.xml']
    },
    install_requires=[
        'enum-compat>=0.0.3',
        'pyserial>=3.5',
        'beautifulsoup4>=4.12.3',
        'lxml>=5.3.0',
    ])
