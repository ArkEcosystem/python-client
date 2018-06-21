import responses

from ark import ArkClient


def test_count_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/count',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.count()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/count'


def test_search_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.search('my-query')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/delegates/search?')
    assert 'q=my-query' in responses.calls[0].request.url
    assert 'limit=20' in responses.calls[0].request.url


def test_search_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.search('my-query', limit=69, offset=123)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/delegates/search?')
    assert 'q=my-query' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url


def test_get_calls_correct_url_with_passed_in_public_key():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/get',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.get(public_key='my-key')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/get?publicKey=my-key'


def test_get_calls_correct_url_with_passed_in_username():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/get',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.get(username='my-username')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/delegates/get?username=my-username'
    )


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates?limit=20'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.all(limit=69, offset=123, order_by='username')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/delegates?')
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url
    assert 'orderBy=username' in responses.calls[0].request.url


def test_fee_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/fee',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.fee()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/fee'


def test_forged_by_account_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/forging/getForgedByAccount',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.forged_by_account('my-key')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/delegates/forging/getForgedByAccount?generatorPublicKey=my-key'
    )


def test_next_forgers_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/getNextForgers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.delegates.next_forgers()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/getNextForgers'
