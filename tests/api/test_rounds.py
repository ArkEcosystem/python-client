import responses
from client import Client


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/rounds',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.rounds.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/rounds'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/rounds',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.rounds.all({
        'query_param1': 'value1',
        'query_param2': 'value2',
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/rounds?')
    assert 'query_param1=value1' in url
    assert 'query_param2=value2' in url


def test_show_calls_correct_url():
    round_id = '12345'
    responses.add(
        responses.GET,
        f'http://127.0.0.1:4002/api/rounds/{round_id}',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.rounds.show(round_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/rounds/12345'
    )


def test_validators_calls_correct_url():
    round_id = '12345'
    responses.add(
        responses.GET,
        f'http://127.0.0.1:4002/api/rounds/{round_id}/validators',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.rounds.validators(round_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/rounds/12345/validators'
    )
