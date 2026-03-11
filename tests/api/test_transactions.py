import json

import responses

from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.transactions.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/transactions'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.transactions.all({
        'page': 5,
        'limit': 69,
        'orderBy': 'timestamp.epoch',
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/transactions?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url
    assert 'orderBy=timestamp.epoch' in url


def test_create_calls_correct_url_with_data():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/tx/api/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/tx/api')
    client.transactions.create([{'random': 'data'}])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/tx/api/transactions'
    )
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'transactions': [{'random': 'data'}]
    }


def test_get_calls_correct_url():
    transaction_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/transactions/{}'.format(
            transaction_id
        ),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.transactions.get(transaction_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/transactions/12345'
    )


def test_all_unconfirmed_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/transactions/unconfirmed',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.transactions.all_unconfirmed()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/transactions/unconfirmed'
    )


def test_all_unconfirmed_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/transactions/unconfirmed',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.transactions.all_unconfirmed({
        'page': 5,
        'limit': 69,
        'orderBy': 'timestamp.epoch',
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/transactions/unconfirmed?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url
    assert 'orderBy=timestamp.epoch' in url


def test_get_unconfirmed_calls_correct_url():
    transaction_id = '12345'

    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/transactions/unconfirmed/{}'.format(
            transaction_id
        ),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.transactions.get_unconfirmed(transaction_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/transactions/unconfirmed/12345'
    )


def test_configuration_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/tx/api/configuration',
        json={'success': True},
        status=200
    )

    client = ArkClient({
        'api': 'http://127.0.0.1:4002/api',
        'transactions': 'http://127.0.0.1:4002/tx/api',
        'evm': None,
    })
    client.transactions.configuration()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/tx/api/configuration'
    )
