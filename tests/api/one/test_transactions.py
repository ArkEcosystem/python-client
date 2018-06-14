import responses

from ark import ArkClient


def test_get_calls_correct_url_with_passed_in_param():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/get',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.transactions.get('my-transaction')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/transactions/get?id=my-transaction'
    )


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
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

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.transactions.all(limit=69, offset=123)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/transactions?'
    )
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url


def test_get_unconfirmed_calls_correct_url_with_passed_in_param():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/unconfirmed/get',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.transactions.get_unconfirmed('my-transaction')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/transactions/unconfirmed/get?id=my-transaction'
    )


def test_all_unconfirmed_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/transactions/unconfirmed',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
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

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.transactions.all_unconfirmed(limit=69, offset=123)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/transactions/unconfirmed?'
    )
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url
