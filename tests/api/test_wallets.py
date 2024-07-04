import json

import responses

from client import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/wallets?limit=100'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/wallets?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_top_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/top',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.top()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/wallets/top?limit=100'


def test_top_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/top',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.top(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/wallets/top?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_get_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.get(wallet_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/wallets/12345'

def test_transactions_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/transactions'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.transactions(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/wallets/12345/transactions?limit=100'
    )


def test_transactions_calls_correct_url_with_additional_params():
    wallet_id = '12345'
    responses.add(
      responses.GET,
      'http://127.0.0.1:4002/wallets/{}/transactions'.format(wallet_id),
      json={'success': True},
      status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.transactions(wallet_id=wallet_id, page=5, limit=69, orderBy="timestamp.epoch")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/wallets/12345/transactions?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert 'orderBy=timestamp.epoch' in responses.calls[0].request.url


def test_transactions_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/transactions'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.transactions(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/wallets/12345/transactions?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_transactions_sent_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/transactions/sent'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.transactions_sent(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/wallets/12345/transactions/sent?limit=100'
    )


def test_transactions_sent_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/transactions/sent'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.transactions_sent(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/wallets/12345/transactions/sent?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_transactions_received_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/transactions/received'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.transactions_received(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/wallets/12345/transactions/received?limit=100'
    )


def test_transactions_received_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/transactions/received'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.transactions_received(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/wallets/12345/transactions/received?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_votes_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/votes'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.votes(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/wallets/12345/votes?limit=100'
    )


def test_votes_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/wallets/{}/votes'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.wallets.votes(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/wallets/12345/votes?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
