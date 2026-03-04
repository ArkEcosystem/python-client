import responses

from client import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/tokens?limit=100'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/api/tokens?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


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


def test_holders_calls_correct_url_with_default_params():
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
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/holders?limit=100'
    )


def test_holders_calls_correct_url_with_passed_in_params():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/holders'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.holders(address, page=3, limit=50)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/holders?'
    )
    assert 'page=3' in responses.calls[0].request.url
    assert 'limit=50' in responses.calls[0].request.url


def test_transfers_calls_correct_url_with_default_params():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/transfers'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers(address)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/transfers?limit=100'
    )


def test_transfers_calls_correct_url_with_passed_in_params():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/transfers'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers(address, page=2, limit=25)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/transfers?'
    )
    assert 'page=2' in responses.calls[0].request.url
    assert 'limit=25' in responses.calls[0].request.url


def test_all_transfers_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/transfers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.all_transfers()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/transfers?limit=100'
    )


def test_all_transfers_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/transfers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.all_transfers(page=1, limit=10)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/api/tokens/transfers?'
    )
    assert 'page=1' in responses.calls[0].request.url
    assert 'limit=10' in responses.calls[0].request.url


