# Ark Python - Client

<p align="center">
    <img src="https://github.com/ArkEcosystem/python-client/blob/master/banner.png" />
</p>

> A simple Python API client for the Ark Blockchain.

[![Build Status](https://badgen.now.sh/circleci/github/ArkEcosystem/python-client)](https://circleci.com/gh/ArkEcosystem/python-client)
[![Codecov](https://badgen.now.sh/codecov/c/github/arkecosystem/python-client)](https://codecov.io/gh/arkecosystem/python-client)
[![Latest Version](https://badgen.now.sh/github/release/ArkEcosystem/python-client)](https://github.com/ArkEcosystem/python-client/releases/latest)
[![License: MIT](https://badgen.now.sh/badge/license/MIT/green)](https://opensource.org/licenses/MIT)

> Lead Maintainer: [Brian Faust](https://github.com/faustbrian)

## Guide for contributing

1. Fork the repository on GitHub.
2. Run the tests to confirm they all pass on your system. If they don’t, you’ll need to investigate why they fail. If you’re unable to diagnose this yourself raise it as a bug report.
3. Make your change.
4. Write tests that demonstrate your bug or feature.
5. Run the entire test suite again, confirming that all tests pass including the ones you just added.
6. Send a GitHub Pull Request. GitHub Pull Requests are the expected method of code collaboration on this project.

If you have any questions, requests or ideas open an issue or ask us in #python on the [ArkEcosystem Slack](https://ark.io/slack).

## Development

### Prerequisites

- Python 3.7

### Setup

1. **Create a virtual environment**

Run the following command to create a virtual environment for the project:

```bash
python -m venv venv
```

2. Activate the virtual environment

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows

```bash
.\venv\Scripts\activate
```

3. Upgrade pip and setuptools

Ensure you have the latest versions of pip and setuptools:

```bash
pip install --upgrade pip setuptools
```

4. Install the dependencies

Install all necessary dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```

5. Install the package in development mode

Run the following command to install the package in development mode:

```bash
python setup.py develop
```

6. Run the tests

Use pytest to run the tests and ensure everything is working correctly:

```bash
python setup.py test
```

Or directly with pytest:

```bash
pytest
```

## Documentation

You can find installation instructions and detailed instructions on how to use this package at the [dedicated documentation site](https://docs.ark.io/sdk/clients/usage.html).

## Security

If you discover a security vulnerability within this package, please send an e-mail to security@ark.io. All security vulnerabilities will be promptly addressed.

## Credits

This project exists thanks to all the people who [contribute](../../contributors).

## License

[MIT](LICENSE) © [ARK Ecosystem](https://ark.io)
