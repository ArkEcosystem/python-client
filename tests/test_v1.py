import pytest

import tests.env as env

from ark.ark import ArkClient


VERSION = '1.1.1'
API_VERSION = 'v1'

ARK = ArkClient(
    env.HOST,
    env.PORT,
    env.NETHASH,
    VERSION,
    api_version=API_VERSION
)


# Account

def test_account_balance():
    res = ARK.accounts().balance(env.ADDRESS)
    assert res['success'] is True
    assert 'balance' in res
    assert 'unconfirmedBalance' in res


def test_account_public_key():
    res = ARK.accounts().public_key(env.ADDRESS)
    assert res['success'] is True
    assert res['publicKey'] == env.PUBLIC_KEY


def test_account_delegates():
    res = ARK.accounts().delegates(env.ADDRESS)
    assert res['success'] is True
    assert 'delegates' in res


def test_account_delegates_fee():
    res = ARK.accounts().delegates_fee()
    assert res['success'] is True
    assert 'fee' in res


def test_account_account():
    res = ARK.accounts().account(env.ADDRESS)
    assert res['success'] is True
    assert 'account' in res


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_account_accounts():
    res = ARK.accounts().accounts()
    assert res['success'] is True
    assert len(res['accounts']) == 100


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_account_accounts_with_parameters():
    parameters = {'limit': 1}
    res = ARK.accounts().accounts(parameters=parameters)
    assert res['success'] is True
    assert len(res['accounts']) == 1


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_account_top():
    res = ARK.accounts().top()
    assert res['success'] is True
    assert len(res['accounts']) == 100


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_account_top_with_parameters():
    parameters = {'limit': 1}
    res = ARK.accounts().top(parameters=parameters)
    assert res['success'] is True
    assert len(res['accounts']) == 1


@pytest.mark.skip('Server is returning "API error: Cannot convert undefined or null to object"')
def test_account_count():
    res = ARK.accounts().count()
    assert res['success'] is True
    assert 'account' in res


# Block

def test_block_block():
    res = ARK.blocks().block(env.BLOCK_ID)
    assert res['success'] is True
    assert 'block' in res


def test_block_blocks():
    res = ARK.blocks().blocks()
    assert res['success'] is True
    assert 'blocks' in res
    assert len(res['blocks']) == 100


def test_block_blocks_with_parameters():
    parameters = {'limit': 1}
    res = ARK.blocks().blocks(parameters=parameters)
    assert res['success'] is True
    assert 'blocks' in res
    assert len(res['blocks']) == 1


def test_block_epoch():
    res = ARK.blocks().epoch()
    assert res['success'] is True
    assert res['epoch'] == '2017-03-21T13:00:00.000Z'


def test_block_height():
    res = ARK.blocks().height()
    assert res['success'] is True
    assert 'height' in res


def test_block_nethash():
    res = ARK.blocks().nethash()
    assert res['success'] is True
    assert res['nethash'] == env.NETHASH


def test_block_fee():
    res = ARK.blocks().fee()
    assert res['success'] is True
    assert 'fee' in res


def test_block_fees():
    res = ARK.blocks().fees()
    assert res['success'] is True
    assert 'fees' in res


def test_block_milestone():
    res = ARK.blocks().milestone()
    assert res['success'] is True
    assert 'milestone' in res


def test_block_reward():
    res = ARK.blocks().reward()
    assert res['success'] is True
    assert 'reward' in res


def test_block_supply():
    res = ARK.blocks().supply()
    assert res['success'] is True
    assert 'supply' in res


def test_block_status():
    res = ARK.blocks().status()
    assert res['success'] is True
    assert 'epoch' in res
    assert 'height' in res
    assert 'fee' in res
    assert 'milestone' in res
    assert 'reward' in res
    assert 'supply' in res
    assert res['nethash'] == env.NETHASH


# Delegate

def test_delegate_count():
    res = ARK.delegates().count()
    assert res['success'] is True
    assert 'count' in res


def test_delegate_search():
    q = env.DELEGATE_NAME
    res = ARK.delegates().search(q)
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) > 1


def test_delegate_search_with_paremeters():
    q = env.DELEGATE_NAME
    parameters = {'limit': 1}
    res = ARK.delegates().search(q, parameters=parameters)
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) == 1


def test_delegate_voters():
    res = ARK.delegates().voters(env.PUBLIC_KEY)
    assert res['success'] is True
    assert 'accounts' in res


def test_delegate_delegate():
    parameters = {'publicKey': env.PUBLIC_KEY}
    res1 = ARK.delegates().delegate(parameters)
    assert res1['success'] is True
    assert 'delegate' in res1
    parameters = {'username': env.DELEGATE_NAME}
    res2 = ARK.delegates().delegate(parameters)
    assert res1 == res2


def test_delegate_delegates():
    res = ARK.delegates().delegates()
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) == 51


def test_delegate_delegates_with_paremeters():
    parameters = {'limit': 1}
    res = ARK.delegates().delegates(parameters=parameters)
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) == 1


def test_delegate_fee():
    res = ARK.delegates().fee()
    assert res['success'] is True
    assert 'fee' in res


def test_delegate_forged_by_account():
    res = ARK.delegates().forged_by_account(env.PUBLIC_KEY)
    assert res['success'] is True
    assert 'fees' in res
    assert 'rewards' in res
    assert 'forged' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_delegate_create():
    assert False


def test_delegate_next_forgers():
    res = ARK.delegates().next_forgers()
    assert res['success'] is True
    assert 'currentBlock' in res
    assert 'currentSlot' in res
    assert 'delegates' in res


# Loader

def test_loader_status():
    res = ARK.loaders().status()
    assert res['success'] is True
    assert 'loaded' in res
    assert 'now' in res
    assert 'blocksCount' in res


def test_loader_sync():
    res = ARK.loaders().sync()
    assert res['success'] is True
    assert 'syncing' in res
    assert 'blocks' in res
    assert 'height' in res
    assert 'id' in res


def test_loader_autoconfigure():
    res = ARK.loaders().autoconfigure()
    assert res['success'] is True
    assert 'network' in res


# Peer

def test_peer_peer():
    ip = env.HOST
    port = env.PORT
    res = ARK.peers().peer(ip, port)
    assert res['success'] is True
    assert 'peer' in res
    assert res['peer']['ip'] == ip
    assert res['peer']['port'] == port
    assert res['peer']['version'] == VERSION


def test_peer_peers():
    res = ARK.peers().peers()
    assert res['success'] is True
    assert 'peers' in res
    assert len(res['peers']) > 1


def test_peer_peers_with_parameters():
    parameters = {'status': 'OK'}
    res = ARK.peers().peers(parameters)
    assert res['success'] is True
    assert 'peers' in res
    statuses_are_ok = [peer['status'] == 'OK' for peer in res['peers']]
    assert all(statuses_are_ok)


def test_peer_version():
    res = ARK.peers().version()
    assert res['success'] is True
    assert res['version'] == VERSION


# Signature

def test_signature_fee():
    res = ARK.signatures().fee()
    assert res['success'] is True
    assert 'fee' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_signature_create():
    assert False


# Transaction

def test_transaction_transaction():
    res = ARK.transactions().transaction(env.TRANSACTION_ID)
    assert res['success'] is True
    assert 'transaction' in res


def test_transaction_transactions():
    res = ARK.transactions().transactions()
    assert res['success'] is True
    assert 'transactions' in res
    assert len(res['transactions']) > 1


def test_transaction_transactions_with_parameters():
    parameters = {'limit': 1, 'offset': 0}
    res = ARK.transactions().transactions(parameters)
    assert res['success'] is True
    assert 'transactions' in res
    assert len(res['transactions']) == 1


@pytest.mark.skip('Need to create transaction to test unconrfirmed transaction')
def test_transaction_unconfirmed_transaction():
    parameters = {'orderBy': 'timestamp:desc',
                  'limit': 1}
    res = ARK.transactions().transactions(parameters)
    assert res['success'] is True
    id_ = res['transactions'][0]['id']
    res = ARK.transactions().unconfirmed_transaction(id_)
    assert res['success'] is True
    assert 'transaction' in res


def test_transaction_unconfirmed_transactions():
    res = ARK.transactions().unconfirmed_transactions()
    assert res['success'] is True
    assert 'transactions' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_transaction_create():
    assert False


# Transport

def test_transport_list():
    res = ARK.transport().list()
    assert res['success'] is True
    assert 'peers' in res


@pytest.mark.skip('Server returns Expected type string but found type integer: #/ids')
def test_transport_blocks_common():
    ids = [env.BLOCK_ID]
    res = ARK.transport().blocks_common(ids)
    assert res['success'] is True
    assert 'common' in res
    assert 'lastBlockHeight' in res


def test_transport_blocks_common_multiple():
    ids = [env.BLOCK_ID, env.NEXT_BLOCK_ID]
    res = ARK.transport().blocks_common(ids)
    assert res['success'] is True
    assert 'common' in res
    assert 'lastBlockHeight' in res


@pytest.mark.skip('Server not returning "success" obj in JSON.')
def test_transport_block():
    res = ARK.transport().block(env.BLOCK_ID)
    assert res['success'] is True
    assert 'block' in res


def test_transport_blocks():
    res = ARK.transport().blocks()
    assert res['success'] is True
    assert 'blocks' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_transport_create_block():
    assert False


def test_transport_transactions():
    res = ARK.transport().transactions()
    assert res['success'] is True
    assert 'transactions' in res


def test_transport_transactions_from_ids():
    ids = [env.TRANSACTION_ID]
    res = ARK.transport().transactions_from_ids(ids)
    assert res['success'] is True
    assert 'transactions' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_transport_create_transaction():
    assert False


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_transport_create_batch_transaction():
    assert False


def test_transport_height():
    res = ARK.transport().height()
    assert res['success'] is True
    assert 'height' in res
    assert 'header' in res


def test_transport_status():
    res = ARK.transport().status()
    assert res['success'] is True
    assert 'height' in res
    assert 'forgingAllowed' in res
    assert 'currentSlot' in res
    assert 'header' in res


# Vote

@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_vote_vote():
    assert False


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_vote_unvote():
    assert False
