import responses

from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/validators',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.validators.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/validators'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/validators',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.validators.all({
        'page': 5,
        'limit': 69,
        'orderBy': 'username',
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/validators?'
    )
    assert 'page=5' in url
    assert 'limit=69' in url
    assert 'orderBy=username' in url


def test_get_calls_correct_url():
    validator_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/validators/{}'.format(validator_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.validators.get(validator_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/validators/12345'
    )


def test_blocks_calls_correct_url():
    validator_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/validators/{}/blocks'.format(
            validator_id
        ),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.validators.blocks(validator_id, {
        'limit': 100,
        'orderBy': 'timestamp:desc',
    })

    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/validators/12345/blocks?'
    )
    assert 'limit=100' in url
    assert 'orderBy=timestamp%3Adesc' in url


def test_voters_calls_correct_url():
    validator_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/validators/{}/voters'.format(
            validator_id
        ),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.validators.voters(validator_id, {
        'limit': 100,
        'orderBy': 'timestamp:desc',
    })

    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(
        'http://127.0.0.1:4002/api/validators/12345/voters?'
    )
    assert 'limit=100' in url
    assert 'orderBy=timestamp%3Adesc' in url
