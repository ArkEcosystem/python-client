import responses
from client import ArkClient


def test_blockchain_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/blockchain',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.blockchain.blockchain()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/blockchain'
