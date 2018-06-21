import responses

from ark import ArkClient


def test_balance_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/getBalance',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.balance(address='spongebob')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/accounts/getBalance?address=spongebob'
    )


def test_public_key_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/getPublicKey',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.public_key(address='spongebob')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/accounts/getPublicKey?address=spongebob'
    )


def test_delegates_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/delegates',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.delegates(address='spongebob')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/accounts/delegates?address=spongebob'
    )


def test_delegates_fee_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/delegates/fee',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.delegates_fee()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/accounts/delegates/fee'


def test_get_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.get(address='spongebob')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/accounts?address=spongebob'


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/getAllAccounts',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/accounts/getAllAccounts?limit=20'
    )


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/getAllAccounts',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.all(limit=69, offset=123)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/accounts/getAllAccounts?'
    )
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url


def test_top_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/top',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.top()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/accounts/top?limit=20'


def test_top_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/top',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.top(limit=69, offset=123)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/accounts/top?')
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url


def test_count_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/accounts/count',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.accounts.count()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/accounts/count'
