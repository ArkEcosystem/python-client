import responses

from client import Client


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.all({'page': 5, 'limit': 69})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/wallets?')
    assert 'page=5' in url
    assert 'limit=69' in url


def test_top_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/top',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.top()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/top'
    )


def test_top_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/top',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.top({'page': 5, 'limit': 69})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/wallets/top?')
    assert 'page=5' in url
    assert 'limit=69' in url


def test_get_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.get(wallet_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345'
    )


def test_transactions_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions'.format(
            wallet_id
        ),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.transactions(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/transactions'
    )


def test_transactions_calls_correct_url_with_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions'.format(
            wallet_id
        ),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.transactions(wallet_id, {
        'page': 5,
        'limit': 69,
        'orderBy': 'timestamp.epoch',
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/transactions?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url
    assert 'orderBy=timestamp.epoch' in url


def test_sent_transactions_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/sent'.format(
            wallet_id
        ),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.sent_transactions(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/transactions/sent'
    )


def test_sent_transactions_calls_correct_url_with_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/sent'.format(
            wallet_id
        ),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.sent_transactions(wallet_id, {
        'page': 5,
        'limit': 69,
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/transactions/sent?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url


def test_received_transactions_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/received'
        .format(wallet_id),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.received_transactions(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/transactions/received'
    )


def test_received_transactions_calls_correct_url_with_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/transactions/received'
        .format(wallet_id),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.received_transactions(wallet_id, {
        'page': 5,
        'limit': 69,
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345'
        '/transactions/received?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url


def test_votes_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/votes'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.votes(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/votes'
    )


def test_votes_calls_correct_url_with_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/votes'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.votes(wallet_id, {'page': 5, 'limit': 69})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/votes?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url


def test_tokens_for_calls_correct_url():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/tokens'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.tokens_for(wallet_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/wallets/12345/tokens'
    )


def test_tokens_for_calls_correct_url_with_params():
    wallet_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/{}/tokens'.format(wallet_id),
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.tokens_for(wallet_id, {'page': 5, 'limit': 69})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/wallets/12345/tokens?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url


def test_tokens_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/tokens',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.tokens({'addresses': '0xabc,0xdef'})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/wallets/tokens?'
    )
    assert 'addresses=0xabc%2C0xdef' in url


def test_tokens_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/wallets/tokens',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.wallets.tokens({
        'addresses': '0xabc,0xdef',
        'page': 2,
        'limit': 50,
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/wallets/tokens?'
    )
    assert 'page=2' in url
    assert 'limit=50' in url
