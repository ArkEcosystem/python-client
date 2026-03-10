import responses

from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.all({'page': 5, 'limit': 69})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/tokens?')
    assert 'page=5' in url
    assert 'limit=69' in url


def test_get_calls_correct_url():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.get(address)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef'
    )


def test_holders_calls_correct_url():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/holders'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.holders(address)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/holders'
    )


def test_holders_calls_correct_url_with_params():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/holders'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.holders(address, {'page': 3, 'limit': 50})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/holders?'
    )
    assert 'page=3' in url
    assert 'limit=50' in url


def test_transfers_by_token_calls_correct_url():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/transfers'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers_by_token(address)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/transfers'
    )


def test_transfers_by_token_calls_correct_url_with_params():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/transfers'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers_by_token(address, {'page': 2, 'limit': 25})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/transfers?'
    )
    assert 'page=2' in url
    assert 'limit=25' in url


def test_transfers_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/transfers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/transfers'
    )


def test_transfers_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/transfers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers({'page': 1, 'limit': 10})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/tokens/transfers?'
    )
    assert 'page=1' in url
    assert 'limit=10' in url
