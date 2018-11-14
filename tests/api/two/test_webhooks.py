import json
from urllib.parse import urlencode

import responses

from client import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4004/webhooks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks?limit=20'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4004/webhooks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4004/webhooks?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_get_calls_correct_url():
    webhook_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.get(webhook_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/12345'


def test_create_calls_correct_url_with_no_enabled_param():
    event = 'event'
    target = 'target'
    conditions = []
    responses.add(
        responses.POST,
        'http://127.0.0.1:4004/webhooks',
        json={'success': True},
        status=201
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.create(event, target, conditions)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'event': event, 'target': target, 'conditions': conditions, 'enabled': None
    }


def test_create_calls_correct_url_with_enabled_param():
    event = 'event'
    target = 'target'
    conditions = []
    enabled = True
    responses.add(
        responses.POST,
        'http://127.0.0.1:4004/webhooks',
        json={'success': True},
        status=201
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.create(event, target, conditions, enabled=enabled)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'event': event, 'target': target, 'conditions': conditions, 'enabled': enabled
    }


def test_update_calls_correct_url_with_event_param():
    webhook_id = '12345'
    event = 'event'
    responses.add(
        responses.PUT,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=204
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.update(webhook_id, event=event)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/12345'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'event': event
    }


def test_update_calls_correct_url_with_target_param():
    webhook_id = '12345'
    target = 'target'
    responses.add(
        responses.PUT,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=204
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.update(webhook_id, target=target)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/12345'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'target': target
    }


def test_update_calls_correct_url_with_conditions_param():
    webhook_id = '12345'
    conditions = []
    responses.add(
        responses.PUT,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=204
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.update(webhook_id, conditions=conditions)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/12345'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'conditions': conditions
    }


def test_update_calls_correct_url_with_enabled_param():
    webhook_id = '12345'
    enabled = True
    responses.add(
        responses.PUT,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=204
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.update(webhook_id, enabled=enabled)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/12345'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'enabled': enabled
    }


def test_delete_calls_correct_url():
    webhook_id = '12345'
    responses.add(
        responses.DELETE,
        'http://127.0.0.1:4004/webhooks/{}'.format(webhook_id),
        json={'success': True},
        status=204
    )

    client = ArkClient('http://127.0.0.1:4004', api_version='v2')
    client.webhooks.delete(webhook_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4004/webhooks/12345'
