import responses

from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/blocks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.blocks.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/blocks'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/blocks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.blocks.all({
        'page': 5,
        'limit': 69,
        'orderBy': 'timestamp.epoch',
        'number': 6838329,
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/blocks?')
    assert 'page=5' in url
    assert 'limit=69' in url
    assert 'orderBy=timestamp.epoch' in url
    assert 'number=6838329' in url


def test_get_calls_correct_url():
    block_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/blocks/{}'.format(block_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.blocks.get(block_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/blocks/12345'
    )


def test_first_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/blocks/first',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.blocks.first()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/blocks/first'
    )


def test_last_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/blocks/last',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.blocks.last()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/blocks/last'
    )


def test_transactions_calls_correct_url_with_params():
    block_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/blocks/{}/transactions'.format(
            block_id
        ),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.blocks.transactions(block_id, {
        'page': 5,
        'limit': 69,
        'orderBy': 'timestamp.epoch',
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/blocks/12345/transactions?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url
    assert 'orderBy=timestamp.epoch' in url
