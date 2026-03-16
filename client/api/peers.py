from typing import Optional

from client.resource import Resource
from client.types.peers import PeersQuery


class Peers(Resource):

    def all(self, query: Optional[PeersQuery] = None):
        return self.with_endpoint('api').request_get('peers', query)

    def get(self, ip: str):
        return self.with_endpoint('api').request_get(f'peers/{ip}')
