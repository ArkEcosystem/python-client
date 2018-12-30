import json

import responses

from client import ArkClient


def test_get_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4004/webhooks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004')
    client.webhooks.get()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks?limit=100'


def test_get_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4004/webhooks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004')
    client.webhooks.get(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4004/webhooks?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_retrieve_calls_correct_url():
    webhook_id = 1
    responses.add(
        responses.GET,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004')
    client.webhook.retrieve(webhook_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/1'

##### ADD CREATE TESTS
##### UPDATE PUT REQUESTS
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
    webhook_id = '1'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004')
    client.webhooks.delete(webhook_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/1'
