# ARK Python - Client

<p align="center">
    <img src="https://github.com/ArkEcosystem/python-client/blob/master/banner.png" />
</p>

> A simple Python API client for the ARK Blockchain.

[![Build Status](https://img.shields.io/travis/ArkEcosystem/python-client/master.svg?style=flat-square)](https://travis-ci.org/ArkEcosystem/python-client)
[![Latest Version](https://img.shields.io/github/release/ArkEcosystem/python-client.svg?style=flat-square)](https://github.com/ArkEcosystem/python-client/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
git clone https://github.com/ArkEcosystem/python-client
cd python-client
sudo install setup.py
```

## Usage
```bash
from park.park import Park

park = Park(
    '127.0.0.1',
    4003,
    '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
    '2.0.0'
)

delegates = park.park.delegates().delegates()
```

## To Do

```bash
add docstrings for parameters
add v2 API calls
add P2P API calls
fix Peer().peer()
fix both UnconfirmedTransactions functions in Transaction()
Transport function is wonky when installed
error handling
```

## Security

If you discover a security vulnerability within this package, please send an e-mail to security@ark.io. All security vulnerabilities will be promptly addressed.

## Credits

- [Brian Faust](https://github.com/faustbrian)
- [All Contributors](../../../../contributors)

## License

[MIT](LICENSE) © [ArkEcosystem](https://ark.io)
