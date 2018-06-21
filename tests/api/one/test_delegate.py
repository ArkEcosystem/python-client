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


def test_count():
    res = ARK.delegate.count()
    assert res['success'] is True
    assert 'count' in res


def test_search():
    q = env.DELEGATE_NAME
    res = ARK.delegate.search(q)
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) > 1


def test_search_with_paremeters():
    q = env.DELEGATE_NAME
    parameters = {'limit': 1}
    res = ARK.delegate.search(q, parameters=parameters)
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) == 1


def test_voters():
    res = ARK.delegate.voters(env.PUBLIC_KEY)
    assert res['success'] is True
    assert 'accounts' in res


def test_delegate():
    parameters = {'publicKey': env.PUBLIC_KEY}
    res1 = ARK.delegate.delegate(parameters)
    assert res1['success'] is True
    assert 'delegate' in res1
    parameters = {'username': env.DELEGATE_NAME}
    res2 = ARK.delegate.delegate(parameters)
    assert res1 == res2


def test_delegates():
    res = ARK.delegate.delegates()
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) == 51


def test_delegates_with_paremeters():
    parameters = {'limit': 1}
    res = ARK.delegate.delegates(parameters=parameters)
    assert res['success'] is True
    assert 'delegates' in res
    assert len(res['delegates']) == 1


def test_fee():
    res = ARK.delegate.fee()
    assert res['success'] is True
    assert 'fee' in res


def test_forged_by_account():
    res = ARK.delegate.forged_by_account(env.PUBLIC_KEY)
    assert res['success'] is True
    assert 'fees' in res
    assert 'rewards' in res
    assert 'forged' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_create():
    assert False


def test_next_forgers():
    res = ARK.delegate.next_forgers()
    assert res['success'] is True
    assert 'currentBlock' in res
    assert 'currentSlot' in res
    assert 'delegates' in res
