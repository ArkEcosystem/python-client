import json

import responses

from client import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/wallets?limit=100'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/api/wallets?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_top_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/top',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.top()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/wallets/top?limit=100'


def test_top_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/top',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.top(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/api/wallets/top?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_get_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.get(wallet_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/wallets/12345'

def test_transactions_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.transactions(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/transactions?limit=100'
    )


def test_transactions_calls_correct_url_with_additional_params():
    wallet_id = '12345'
    responses.add(
      responses.GET,
      'http://127.0.0.1:4002/api/wallets/{}/transactions'.format(wallet_id),
      json={'success': True},
      status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.transactions(wallet_id=wallet_id, page=5, limit=69, orderBy="timestamp.epoch")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/api/wallets/12345/transactions?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert 'orderBy=timestamp.epoch' in responses.calls[0].request.url


def test_transactions_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.transactions(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/transactions?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_sent_transactions_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/sent'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.sent_transactions(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/transactions/sent?limit=100'
    )


def test_sent_transactions_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/sent'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.sent_transactions(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/transactions/sent?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_received_transactions_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/received'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.received_transactions(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/transactions/received?limit=100'
    )


def test_received_transactions_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/received'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.received_transactions(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/transactions/received?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_votes_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/votes'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.votes(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/votes?limit=100'
    )


def test_votes_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/votes'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.votes(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/votes?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_tokens_calls_correct_url_with_default_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/tokens'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.tokens(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/tokens?limit=100'
    )


def test_tokens_calls_correct_url_with_passed_in_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/tokens'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.tokens(wallet_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/tokens?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_tokens_for_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/tokens',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.tokens_for('0xabc,0xdef')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/wallets/tokens?'
    )
    assert 'addresses=0xabc%2C0xdef' in responses.calls[0].request.url
    assert 'limit=100' in responses.calls[0].request.url


def test_tokens_for_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/tokens',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.wallets.tokens_for('0xabc,0xdef', page=2, limit=50)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/wallets/tokens?'
    )
    assert 'page=2' in responses.calls[0].request.url
    assert 'limit=50' in responses.calls[0].request.url
