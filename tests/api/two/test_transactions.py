import json

import responses

from ark import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/transactions?limit=20'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/transactions?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_create_calls_correct_url_with_data():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.create([{'random': 'data'}])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/transactions'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'transactions': [{'random': 'data'}]
    }


def test_get_calls_correct_url():
    transaction_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/{}'.format(transaction_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.get(transaction_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/transactions/12345'


def test_all_unconfirmed_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/unconfirmed',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.all_unconfirmed()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/transactions/unconfirmed?limit=20'
    )


def test_all_unconfirmed_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/unconfirmed',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.all_unconfirmed(offset=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/transactions/unconfirmed?'
    )
    assert 'offset=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_search_calls_correct_url_with_default_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/transactions/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.search({'blockId': '1337'})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/transactions/search?limit=20'
    assert json.loads(responses.calls[0].request.body.decode()) == {'blockId': '1337'}


def test_search_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/transactions/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.search({'blockId': '1337'}, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/transactions/search?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert json.loads(responses.calls[0].request.body.decode()) == {'blockId': '1337'}


def test_transaction_types():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/types',
        json={
            'data': {
                'TRANSFER': 0,
                'SECOND_SIGNATURE': 1,
                'DELEGATE_REGISTRATION': 2,
                'VOTE': 3,
                'MULTI_SIGNATURE': 4,
                'IPFS': 5,
                'TIMELOCK_TRANSFER': 6,
                'MULTI_PAYMENT': 7,
                'DELEGATE_RESIGNATION': 8
            }
        },
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.types()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/transactions/types')


def test_transaction_fees():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/fees',
        json={
            'data': {
                'dynamic': False,
                'transfer': 10000000,
                'secondSignature': 500000000,
                'delegateRegistration': 2500000000,
                'vote': 100000000,
                'multiSignature': 500000000,
                'ipfs': 0,
                'timelockTransfer': 0,
                'multiPayment': 0,
                'delegateResignation': 0
            }
        },
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.transactions.fees()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/transactions/fees')
