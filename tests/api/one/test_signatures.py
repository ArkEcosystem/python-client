import responses

from ark import ArkClient


def test_fee_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/signatures/fee',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.signatures.fee()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/signatures/fee'
