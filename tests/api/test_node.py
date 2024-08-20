import responses

from client import ArkClient


def test_status_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/node/status',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.node.status()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/node/status'


def test_syncing_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/node/syncing',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.node.syncing()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/node/syncing'


def test_configuration_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/node/configuration',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.node.configuration()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/node/configuration'


def test_configuration_crypto_call_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/node/configuration/crypto',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.node.crypto()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/node/configuration/crypto'

def test_fees_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/node/fees',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.node.fees()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/node/fees'


def test_fees_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/node/fees',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.node.fees(days=14)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/api/node/fees?')
    assert 'days=14' in responses.calls[0].request.url
