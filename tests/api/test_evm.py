import json
import responses

from client import ArkClient


def test_eth_call_methods_correct_url():
    responses.add(
        responses.POST,
        'http://127.0.0.1:4002/evm/api/',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/evm/api')
    client.evm.eth_call([{ 'random': 'data' }])
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/evm/api/'
    assert json.loads(responses.calls[0].request.body.decode()) == {
        'jsonrpc': '2.0',
        'method': 'eth_call',
        'params': [[{ 'random': 'data' }], 'latest'],
        'id': None,
    }
