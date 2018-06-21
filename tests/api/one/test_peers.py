import responses

from ark import ArkClient


def test_get_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/peers/get',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.peers.get('127.0.0.1', 1234)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/peers/get?')
    assert 'ip=127.0.0.1' in responses.calls[0].request.url
    assert 'port=1234' in responses.calls[0].request.url


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/peers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.peers.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/peers?limit=20'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/peers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.peers.all(limit=69, offset=123)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/peers?')
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url


def test_version_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/peers/version',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.peers.version()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/peers/version'
