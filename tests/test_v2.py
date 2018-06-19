import pytest

import tests.env as env

from ark.ark import ArkClient


VERSION = '2.0'
API_VERSION = 'v2'

ARK = ArkClient(
    env.HOST,
    env.PORT,
    env.NETHASH,
    VERSION,
    api_version=API_VERSION
)


def test_accounts():
    with pytest.raises(NotImplementedError):
        ARK.accounts()


def test_blocks():
    with pytest.raises(NotImplementedError):
        ARK.blocks()


def test_delegates():
    with pytest.raises(NotImplementedError):
        ARK.delegates()


def test_loaders():
    with pytest.raises(NotImplementedError):
        ARK.loaders()


def test_peers():
    with pytest.raises(NotImplementedError):
        ARK.peers()


def test_signatures():
    with pytest.raises(NotImplementedError):
        ARK.signatures()


def test_transactions():
    with pytest.raises(NotImplementedError):
        ARK.transactions()


def test_transport():
    with pytest.raises(NotImplementedError):
        ARK.transport()


def test_votes():
    with pytest.raises(NotImplementedError):
        ARK.votes()
