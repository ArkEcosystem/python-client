import pytest

import tests.api.one.env as env_v1
import tests.env as env

from ark.client import ArkClient


ARK = ArkClient(
    env.HOST,
    env.PORT,
    env.NETHASH,
    env_v1.VERSION,
    api_version=env_v1.API_VERSION
)


def test_list():
    res = ARK.transport.list()
    assert res['success'] is True
    assert 'peers' in res


@pytest.mark.skip('Server returns Expected type string but found type integer: #/ids')
def test_blocks_common():
    ids = [env.BLOCK_ID]
    res = ARK.transport.blocks_common(ids)
    assert res['success'] is True
    assert 'common' in res
    assert 'lastBlockHeight' in res


def test_blocks_common_multiple():
    ids = [env.BLOCK_ID, env.NEXT_BLOCK_ID]
    res = ARK.transport.blocks_common(ids)
    assert res['success'] is True
    assert 'common' in res
    assert 'lastBlockHeight' in res


@pytest.mark.skip('Server not returning "success" obj in JSON.')
def test_block():
    res = ARK.transport.block(env.BLOCK_ID)
    assert res['success'] is True
    assert 'block' in res


def test_blocks():
    res = ARK.transport.blocks()
    assert res['success'] is True
    assert 'blocks' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_create_block():
    assert False


def test_transactions():
    res = ARK.transport.transactions()
    assert res['success'] is True
    assert 'transactions' in res


def test_transactions_from_ids():
    ids = [env.TRANSACTION_ID]
    res = ARK.transport.transactions_from_ids(ids)
    assert res['success'] is True
    assert 'transactions' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_create_transaction():
    assert False


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_create_batch_transaction():
    assert False


def test_height():
    res = ARK.transport.height()
    assert res['success'] is True
    assert 'height' in res
    assert 'header' in res


def test_status():
    res = ARK.transport.status()
    assert res['success'] is True
    assert 'height' in res
    assert 'forgingAllowed' in res
    assert 'currentSlot' in res
    assert 'header' in res
