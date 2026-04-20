import responses

from client import Client


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/peers',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.peers.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/peers'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/peers',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.peers.all({
        'os': 'a',
        'status': 'live',
        'port': 1337,
        'version': '2.0.0',
        'orderBy': 'ip',
        'page': 5,
        'limit': 69,
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/peers?')
    assert 'os=a' in url
    assert 'status=live' in url
    assert 'port=1337' in url
    assert 'version=2.0.0' in url
    assert 'orderBy=ip' in url
    assert 'page=5' in url
    assert 'limit=69' in url


def test_get_calls_correct_url_with_ip():
    ip = '123.4.5.67'
    responses.add(
        responses.GET,
        f'http://127.0.0.1:4002/api/peers/{ip}',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.peers.get(ip)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/peers/123.4.5.67'
    )
