import pytest

from client.client import ArkClient


def test_client():
    client = ArkClient('http://127.0.0.1:4002')

    assert hasattr(client, 'connection') == True
    assert hasattr(client, 'api_nodes') == True
    assert hasattr(client, 'blockchain') == True
    assert hasattr(client, 'blocks') == True
    assert hasattr(client, 'commits') == True
    assert hasattr(client, 'delegates') == True
    assert hasattr(client, 'node') == True
    assert hasattr(client, 'peers') == True
    assert hasattr(client, 'rounds') == True
    assert hasattr(client, 'transactions') == True
    assert hasattr(client, 'votes') == True
    assert hasattr(client, 'wallets') == True
