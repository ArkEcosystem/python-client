import responses

from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/votes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.votes.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/votes'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/votes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.votes.all({'page': 5, 'limit': 69})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/votes?')
    assert 'page=5' in url
    assert 'limit=69' in url


def test_get_calls_correct_url():
    vote_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/votes/{}'.format(vote_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.votes.get(vote_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/votes/12345'
    )
