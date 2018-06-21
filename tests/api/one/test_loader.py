import responses

from ark import ArkClient


def test_status_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/loader/status',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.loader.status()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/loader/status'


def test_sync_status_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/loader/status/sync',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.loader.sync_status()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/loader/status/sync'


def test_autoconfigure_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/loader/autoconfigure',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.loader.autoconfigure()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/loader/autoconfigure'
