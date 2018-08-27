import json

import responses

from ark import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.blocks.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks?limit=20'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.blocks.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/blocks?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_get_calls_correct_url():
    block_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/{}'.format(block_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.blocks.get(block_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/12345'


def test_transactions_calls_correct_url_with_default_params():
    block_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/{}/transactions'.format(block_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.blocks.transactions(block_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/blocks/12345/transactions?limit=20'
    )


def test_transactions_calls_correct_url_with_passed_in_params():
    block_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/{}/transactions'.format(block_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.blocks.transactions(block_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/blocks/12345/transactions?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_search_calls_correct_url_with_default_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/blocks/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.blocks.search({'previousBlock': '1337'})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/search?limit=20'
    assert json.loads(responses.calls[0].request.body.decode()) == {'previousBlock': '1337'}


def test_search_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/blocks/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.blocks.search({'previousBlock': '1337'}, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/blocks/search?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert json.loads(responses.calls[0].request.body.decode()) == {'previousBlock': '1337'}
