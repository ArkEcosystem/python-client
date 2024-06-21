import json
import responses
from client import ArkClient


def test_api_nodes_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api-nodes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.api_nodes.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api-nodes'


def test_api_nodes_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api-nodes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.api_nodes.all(query_param1='value1', query_param2='value2')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/api-nodes?')
    assert 'query_param1=value1' in responses.calls[0].request.url
    assert 'query_param2=value2' in responses.calls[0].request.url
