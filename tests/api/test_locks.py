import json

import responses

from client import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/locks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/locks?limit=100'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/locks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/locks?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_all_calls_correct_url_with_additional_params():
    responses.add(
      responses.GET,
      'http://127.0.0.1:4002/locks',
      json={'success': True},
      status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.all(page=5, limit=69, orderBy="id")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/locks?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert 'orderBy=id' in responses.calls[0].request.url


def test_get_calls_correct_url():
    lock_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/locks/{}'.format(lock_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.get(lock_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/locks/12345'


def test_search_calls_correct_url_with_default_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/locks/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.search({'id': '1337'})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/locks/search?limit=100'
    assert json.loads(responses.calls[0].request.body.decode()) == {'id': '1337'}


def test_search_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/locks/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.search({'id': '1337'}, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/locks/search?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert json.loads(responses.calls[0].request.body.decode()) == {'id': '1337'}


def test_search_unlocked_correct_url_with_default_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/locks/unlocked',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.unlocked({'id': '1337'})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/locks/unlocked?limit=100'
    assert json.loads(responses.calls[0].request.body.decode()) == {'id': '1337'}


def test_search_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/locks/unlocked',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.locks.unlocked({'id': '1337'}, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/locks/unlocked?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert json.loads(responses.calls[0].request.body.decode()) == {'id': '1337'}
