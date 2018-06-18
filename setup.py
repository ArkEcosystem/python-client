import setuptools

requires = [
    'requests>=2.19.1',
]

tests_require = [
    'flake8>=3.5.0',
    'flake8-import-order>=0.17.1',
    'flake8-quotes>=1.0.0',
]

extras_require = {
    'test': tests_require,
    'dev': requires + tests_require
}

setuptools.setup(
    name='ark-client',
    description='A simple Python API client for the ARK Blockchain.',
    version='0.0.1',
    author='',
    author_email='',
    url='https://github.com/ArkEcosystem/python-client',
    packages=[
        'ark',
        'ark.one',
        'ark.two'
    ],
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
)
