#!/usr/bin/env python

from setuptools import setup

setup(
    name='enocean4ha',
    version='1.0.6',
    description='EnOcean serial protocol implementation',
    long_description='A Python library for reading and controlling EnOcean devices.',
    long_description_content_type="text/plain",
    author='Kimmo Huoman',
    author_email='kipenroskaposti@gmail.com',
    maintainer='topic2k',
    maintainer_email='topic2k@atlogger.de',
    url='https://github.com/topic2k/enocean4ha',
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
