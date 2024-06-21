import responses
from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/rounds',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.rounds.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/rounds'


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/rounds',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.rounds.all(query_param1='value1', query_param2='value2')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/rounds?')
    assert 'query_param1=value1' in responses.calls[0].request.url
    assert 'query_param2=value2' in responses.calls[0].request.url


def test_show_calls_correct_url():
    round_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/rounds/{}'.format(round_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.rounds.show(round_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/rounds/12345'


def test_delegates_calls_correct_url():
    round_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/rounds/{}/delegates'.format(round_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.rounds.delegates(round_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/rounds/12345/delegates'
