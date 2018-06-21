import tests.api.one.env as env_v1
import tests.env as env

from ark.client import ArkClient


ARK = ArkClient(
    env.HOST,
    env.PORT,
    env.NETHASH,
    env_v1.VERSION,
    api_version=env_v1.API_VERSION
)


def test_peer():
    ip = env.HOST
    port = env.PORT
    res = ARK.peers.peer(ip, port)
    assert res['success'] is True
    assert 'peer' in res
    assert res['peer']['ip'] == ip
    assert res['peer']['port'] == port
    assert res['peer']['version'] == env_v1.VERSION


def test_peers():
    res = ARK.peers.peers()
    assert res['success'] is True
    assert 'peers' in res
    assert len(res['peers']) > 1


def test_peers_with_parameters():
    parameters = {'status': 'OK'}
    res = ARK.peers.peers(parameters)
    assert res['success'] is True
    assert 'peers' in res
    statuses_are_ok = [peer['status'] == 'OK' for peer in res['peers']]
    assert all(statuses_are_ok)


def test_version():
    res = ARK.peers.version()
    assert res['success'] is True
    assert res['version'] == env_v1.VERSION
