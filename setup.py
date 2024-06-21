import sys

import setuptools

requires = [
    'atomicwrites==1.4.1',
    'attrs==23.2.0',
    'backoff==2.2.1',
    'certifi==2024.6.2',
    'chardet==3.0.4',
    'flatten_dict==0.4.2',
    'idna==2.7',
    'importlib-metadata==6.7.0',
    'mccabe==0.6.1',
    'more-itertools==9.1.0',
    'pluggy==1.5.0',
    'py==1.11.0',
    'requests==2.19.1',
    'responses==0.10.15',
    'six==1.16.0',
    'typing_extensions==4.7.1',
    'urllib3==1.23',
    'zipp==3.15.0'
]

tests_require = [
    'coverage==7.2.7',
    'flake8==3.5.0',
    'flake8-import-order==0.17.1',
    'flake8-print==3.1.0',
    'flake8-quotes==1.0.0',
    'pycodestyle<2.4.0,>=2.0.0',
    'pyflakes==1.6.0',
    'pytest==8.2.2',
    'pytest-cov==2.5.1',
    'pytest-mock==1.10.0',
    'pytest-responses==0.5.1'
]

extras_require = {
    'test': tests_require,
    'dev': requires + tests_require
}

setup_requires = ['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else []

setuptools.setup(
    name='arkecosystem-client',
    description='A simple Python API client for the ARK Blockchain.',
    version='2.0.0',
    author='Ark Ecosystem',
    author_email='info@client.io',
    url='https://github.com/ArkEcosystem/python-client',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
)
