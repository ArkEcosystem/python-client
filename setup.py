#!/usr/bin/env python

try:
    from setuptools import setup
    import wheel
except ImportError:
    from distutils.core import setup

setup(
    name='python-client',
    description='A simple Python API client for the ARK Blockchain.',
    version='0.0.1',
    author='',
    author_email='',
    url='https://github.com/galperins4/python-client',
    packages=['park', 'park.one', 'park.two', 'park.p2p', 'park.builder', 'park.builder.templates'],
    install_requires=[
        'wheel', 'Naked', 'Jinja2', 'requests', 'pyyaml', 'MarkupSafe',
        'certifi', 'urllib3', 'chardet', 'idna'
    ])
