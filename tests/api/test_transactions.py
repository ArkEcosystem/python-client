import json

import responses

from client import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.transactions.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/transactions?limit=100'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.transactions.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/transactions?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_all_calls_correct_url_with_additional_params():
    responses.add(
      responses.GET,
      'http://127.0.0.1:4002/transactions',
      json={'success': True},
      status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.transactions.all(page=5, limit=69, orderBy="timestamp.epoch")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/transactions?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert 'orderBy=timestamp.epoch' in responses.calls[0].request.url


def test_create_calls_correct_url_with_data():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
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

    client = ArkClient('http://127.0.0.1:4002')
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

    client = ArkClient('http://127.0.0.1:4002')
    client.transactions.all_unconfirmed()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/transactions/unconfirmed?limit=100'
    )


def test_all_unconfirmed_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/unconfirmed',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.transactions.all_unconfirmed(offset=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/transactions/unconfirmed?'
    )
    assert 'offset=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_all_unconfirmed_calls_correct_url_with_additional_params():
    responses.add(
      responses.GET,
      'http://127.0.0.1:4002/transactions/unconfirmed',
      json={'success': True},
      status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.transactions.all_unconfirmed(page=5, limit=69, orderBy="timestamp.epoch")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/transactions/unconfirmed?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert 'orderBy=timestamp.epoch' in responses.calls[0].request.url
