import responses
from client import Client


@responses.activate
def test_show_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/commits/1',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.commits.get(1)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/commits/1'
