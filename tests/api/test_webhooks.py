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
    client.webhooks.retrieve(webhook_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/1'

    
def test_create_calls_correct_url_with_data():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4004/webhooks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004')
    client.webhooks.create('block.forged', '127.0.0.1:5000', [{'random':'data'}], 'true')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/api/webhooks'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'event' : 'block.forged', 'target' : '127.0.0.1:5000', 
        'conditions' : [{'random':'data'}], 'enabled':'true'}


def test_update_calls_correct_url_with_passed_in_params():
    webhook_id = 1
    responses.add(
        responses.PUT,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004')
    client.webhooks.update(webhook_id, 'block.forged', '127.0.0.1:5000', [{'random':'data'}], 'false')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4004/api/webhooks/1')
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'event' : 'block.forged', 'target' : '127.0.0.1:5000', 
        'conditions' : [{'random':'data'}], 'enabled':'false'}


def test_delete_calls_correct_url():
    webhook_id = 1
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
