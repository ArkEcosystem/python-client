import responses

from client import ArkClient


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/entities',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.entities.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/entities?limit=100'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/entities',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.entities.all(
        id='1337', address='address', publicKey='pk', isResigned='false', type=0, subType=0, **{'data.name': 'foo', 'data.ipfsData': 'bar'}, page=5, limit=69
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/entities?')
    assert 'id=1337' in responses.calls[0].request.url
    assert 'address=address' in responses.calls[0].request.url
    assert 'publicKey=pk' in responses.calls[0].request.url
    assert 'isResigned=false' in responses.calls[0].request.url
    assert 'type=0' in responses.calls[0].request.url
    assert 'subType=0' in responses.calls[0].request.url

    assert 'data.name=foo' in responses.calls[0].request.url
    assert 'data.ipfsData=bar' in responses.calls[0].request.url

    assert 'page=5' in responses.calls[0].request.url
    assert 'limit=69' in responses.calls[0].request.url

    print(responses.calls[0].request.url)


def test_get_calls_correct_url():
    entity_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/entities/{}'.format(entity_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.entities.get(entity_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/entities/12345'
