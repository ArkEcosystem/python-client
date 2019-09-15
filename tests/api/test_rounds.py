import json

import responses

from client import ArkClient


def test_delegates_calls_correct_url():
    round_id = '12345'
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/rounds/{}/delegates'.format(round_id),
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002')
    client.rounds.delegates(round_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/rounds/12345/delegates'
