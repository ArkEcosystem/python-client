import sys

import setuptools


requires = [
    'requests>=2.19.1',
    'backoff>=1.6.0',
]

tests_require = [
    'flake8>=3.5.0',
    'flake8-import-order>=0.17.1',
    'flake8-print>=3.1.0',
    'flake8-quotes>=1.0.0',
    'pytest>=3.6.1',
    'pytest-responses>=0.3.0',
    'pytest-mock>=1.10.0',
    'pytest-cov>=2.5.1'
]

extras_require = {
    'test': tests_require,
    'dev': requires + tests_require
}

setup_requires = ['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else []

setuptools.setup(
    name='arkecosystem-client',
    description='A simple Python API client for the ARK Blockchain.',
    version='1.1.0',
    author='Ark Ecosystem',
    author_email='info@client.io',
    url='https://github.com/ArkEcosystem/python-client',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
)
