import responses
from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/contracts',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.contracts.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/contracts'


def test_abi_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/contracts/consensus/some-address/abi',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.contracts.abi('consensus', 'some-address')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/contracts/consensus/some-address/abi'
