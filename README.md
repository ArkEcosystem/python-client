# ARK Python - Client

<p align="center">
    <img src="https://github.com/ArkEcosystem/python-client/blob/master/banner.png" />
</p>

> A simple Python API client for the ARK Blockchain.

[![Build Status](https://img.shields.io/travis/ArkEcosystem/python-client/master.svg?style=flat-square)](https://travis-ci.org/ArkEcosystem/python-client)
[![Latest Version](https://img.shields.io/github/release/ArkEcosystem/python-client.svg?style=flat-square)](https://github.com/ArkEcosystem/python-client/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Contributions are closed

We will not be accepting new PRs until we are happy with the base of the client and until it has good test coverage. We'll let you know on our #python Slack channel once we'll accept PRs again.

## Installation

For current develop branch installation please use the following:

```bash
pip install -e git://github.com/ArkEcosystem/python-client.git@develop#egg=ark-client
```

## Guide for contributing

Before you start contributing please take some time and check our official [Python Development Guidelines](https://github.com/ArkEcosystem/development-guidelines/blob/master/Python/README.md) which follow the widely accepted PEP8 Python Style Guide. 🖋

1. Fork the repository on GitHub.
2. Run the tests to confirm they all pass on your system. If they don’t, you’ll need to investigate why they fail. If you’re unable to diagnose this yourself raise it as a bug report.
3. Make your change.
4. Write tests that demonstrate your bug or feature.
5. Run the entire test suite again, confirming that all tests pass including the ones you just added.
6. Send a GitHub Pull Request. GitHub Pull Requests are the expected method of code collaboration on this project.

If you have any questions, requests or ideas open an issue or ask us in #python on [ARK's Slack](https://ark.io/slack).

## Usage

```py
from ark import ArkClient

client = ArkClient('http://127.0.0.1:4003/api/')

delegates = client.delegates.all()
```

or for V1:

```py
from ark import ArkClient

client = ArkClient('http://127.0.0.1:4002/api/', api_version='v1')

delegates = client.delegates.all()
```

## Security

If you discover a security vulnerability within this package, please send an e-mail to security@ark.io. All security vulnerabilities will be promptly addressed.


## Development environment

To install all development requiremenets, simply run `pip install .[dev]`.


## Credits

- [Rok Halužan](https://github.com/roks0n)
- [Tomaž Šifrer](https://github.com/tsifrer)
- [Brian Faust](https://github.com/faustbrian)
- [All Contributors](../../../../contributors)

## License

[MIT](LICENSE) © [ArkEcosystem](https://ark.io)
