from typing import Optional

from client.resource import Resource
from client.types import PaginatedResponse, Response
from client.types.peers import PeerResponse, PeersQuery


class Peers(Resource):

    def all(self, query: Optional[PeersQuery] = None) -> PaginatedResponse[PeerResponse]:
        return self.with_endpoint('api').request_get('peers', query)

    def get(self, ip: str) -> Response[PeerResponse]:
        return self.with_endpoint('api').request_get(f'peers/{ip}')
