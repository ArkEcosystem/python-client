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


def test_balance():
    res = ARK.account.balance(env.ADDRESS)
    assert res['success'] is True
    assert 'balance' in res
    assert 'unconfirmedBalance' in res


def test_public_key():
    res = ARK.account.public_key(env.ADDRESS)
    assert res['success'] is True
    assert res['publicKey'] == env.PUBLIC_KEY


def test_delegates():
    res = ARK.account.delegates(env.ADDRESS)
    assert res['success'] is True
    assert 'delegates' in res


def test_delegates_fee():
    res = ARK.account.delegates_fee()
    assert res['success'] is True
    assert 'fee' in res


def test_account():
    res = ARK.account.account(env.ADDRESS)
    assert res['success'] is True
    assert 'account' in res


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_accounts():
    res = ARK.account.account()
    assert res['success'] is True
    assert len(res['accounts']) == 100


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_accounts_with_parameters():
    parameters = {'limit': 1}
    res = ARK.account.accounts(parameters=parameters)
    assert res['success'] is True
    assert len(res['accounts']) == 1


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_top():
    res = ARK.account.top()
    assert res['success'] is True
    assert len(res['accounts']) == 100


@pytest.mark.skip('Server is returning "API endpoint was not found"')
def test_top_with_parameters():
    parameters = {'limit': 1}
    res = ARK.account.top(parameters=parameters)
    assert res['success'] is True
    assert len(res['accounts']) == 1


@pytest.mark.skip('Server is returning "API error: Cannot convert undefined or null to object"')
def test_count():
    res = ARK.account.count()
    assert res['success'] is True
    assert 'account' in res
