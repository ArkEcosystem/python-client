import responses

from ark import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/peers',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
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

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.peers.all(
        os='a', status='live', port=1337, version='2.0.0', order_by='ip', page=5, limit=69
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/peers?')
    assert 'os=a' in responses.calls[0].request.url
    assert 'status=live' in responses.calls[0].request.url
    assert 'port=1337' in responses.calls[0].request.url
    assert 'version=2.0.0' in responses.calls[0].request.url
    assert 'orderBy=ip' in responses.calls[0].request.url
    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url


def test_get_calls_correct_url_with_ip():
    ip = '123.4.5.67'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/peers/{}'.format(ip),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.peers.get(ip)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/peers/123.4.5.67'
