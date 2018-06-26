import json

import responses

from ark import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
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

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/delegates?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_get_calls_correct_url():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.get(delegate_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/12345'


def test_search_calls_correct_url_with_default_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/delegates/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.search('deadlock')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/search?limit=20'
    assert json.loads(responses.calls[0].request.body.decode()) == {'username': 'deadlock'}


def test_search_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/delegates/search',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.search('deadlock', page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/delegates/search?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url
    assert json.loads(responses.calls[0].request.body.decode()) == {'username': 'deadlock'}


def test_blocks_calls_correct_url_with_default_params():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}/blocks'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.blocks(delegate_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/delegates/12345/blocks?limit=20'
    )


def test_blocks_calls_correct_url_with_passed_in_params():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}/blocks'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.blocks(delegate_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/delegates/12345/blocks?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_voters_calls_correct_url_with_default_params():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}/voters'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.voters(delegate_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/delegates/12345/voters?limit=20'
    )


def test_bvoters_calls_correct_url_with_passed_in_params():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}/voters'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.voters(delegate_id, page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/delegates/12345/voters?'
    )
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_voter_balances_calls_correct_url_with_default_params():
    delegate_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/delegates/{}/voters/balances'.format(delegate_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.delegates.voter_balances(delegate_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/delegates/12345/voters/balances'
