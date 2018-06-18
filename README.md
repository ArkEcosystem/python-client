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

```bash
pip3 install git+git://github.com/ArkEcosystem/python-client.git
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
from ark.ark import ArkClient

ark = ArkClient(
    '127.0.0.1',
    4003,
    '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
    '2.0.0'
)

delegates = ark.delegates().delegates()
```

## To Do

- [ ] add docstrings for parameters
- [X] add v2 API calls
- [X] add P2P API calls
- [ ] fix Peer().peer() - APIv1
- [ ] fix both UnconfirmedTransactions functions in Transaction() - APIv1
- [X] Transport function is wonky when installed 
- [ ] finish API v2 Post methods (blockSearch, transactionSearch, transaction.Create, walletSearch)
- [ ] error handling
- [ ] add pytests

## Security

If you discover a security vulnerability within this package, please send an e-mail to security@ark.io. All security vulnerabilities will be promptly addressed.


## Development environment

To install all development requiremenets, simply run `pip install .[dev]`.


## Credits

- [Brian Faust](https://github.com/faustbrian)
- [All Contributors](../../../../contributors)

## License

[MIT](LICENSE) © [ArkEcosystem](https://ark.io)
