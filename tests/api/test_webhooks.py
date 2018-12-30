import json

import responses

from client import ArkClient


def test_get_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.delegates.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates?limit=100'


def test_get_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.delegates.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/delegates?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_retrieve_calls_correct_url():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.delegates.get(delegate_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/12345'

##### ADD CREATE TESTS
    
def test_update_calls_correct_url_with_default_params():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}/blocks'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.delegates.blocks(delegate_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/delegates/12345/blocks?limit=100'
    )


def test_update_calls_correct_url_with_passed_in_params():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}/blocks'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.delegates.blocks(delegate_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/delegates/12345/blocks?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_delete_calls_correct_url():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.delegates.get(delegate_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/12345'
