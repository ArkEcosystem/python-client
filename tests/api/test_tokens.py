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


def test_holders_for_calls_correct_url():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/holders'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.holders_for(address)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/holders'
    )


def test_transfers_for_calls_correct_url():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/transfers'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers_for(address)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/transfers'
    )


def test_transfers_for_calls_correct_url_with_params():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/transfers'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.transfers_for(address, {'page': 2, 'limit': 25})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/transfers?'
    )
    assert 'page=2' in url
    assert 'limit=25' in url


def test_approvals_for_calls_correct_url():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/approvals'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.approvals_for(address)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/approvals'
    )


def test_approvals_for_calls_correct_url_with_params():
    address = '0x1234567890abcdef'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/{}/approvals'.format(address),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.approvals_for(address, {'page': 2, 'limit': 25})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/tokens/0x1234567890abcdef/approvals?'
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


def test_approvals_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/approvals',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.approvals()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/approvals'
    )


def test_approvals_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/approvals',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.approvals({'page': 1, 'limit': 10})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/tokens/approvals?'
    )
    assert 'page=1' in url
    assert 'limit=10' in url


def test_whitelist_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/whitelist',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.whitelist()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/tokens/whitelist'
    )


def test_whitelist_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/tokens/whitelist',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.tokens.whitelist({'page': 3, 'limit': 50})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/tokens/whitelist?'
    )
    assert 'page=3' in url
    assert 'limit=50' in url
