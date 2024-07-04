import responses
from client import ArkClient


@responses.activate
def test_show_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/commits/1',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.commits.show(1)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/commits/1'
