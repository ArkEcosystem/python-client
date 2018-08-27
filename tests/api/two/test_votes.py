import responses

from ark import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/votes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.votes.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/votes?limit=20'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/votes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.votes.all(page=5, limit=69)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/votes?')
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_get_calls_correct_url():
    vote_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/votes/{}'.format(vote_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.votes.get(vote_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/votes/12345'
