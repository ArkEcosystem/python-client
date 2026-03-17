from typing import Optional

from client.resource import Resource
from client.types import Response
from client.types.node import (
    NodeConfigurationResponse,
    NodeCryptoResponse,
    NodeFeesQuery,
    NodeFeesResponse,
    NodeStatusResponse,
    NodeSyncingResponse,
)


class Node(Resource):

    def status(self) -> Response[NodeStatusResponse]:
        return self.with_endpoint('api').request_get('node/status')

    def syncing(self) -> Response[NodeSyncingResponse]:
        return self.with_endpoint('api').request_get('node/syncing')

    def configuration(self) -> Response[NodeConfigurationResponse]:
        return self.with_endpoint('api').request_get('node/configuration')

    def crypto(self) -> Response[NodeCryptoResponse]:
        return self.with_endpoint('api').request_get('node/configuration/crypto')

    def fees(self, query: Optional[NodeFeesQuery] = None) -> Response[NodeFeesResponse]:
        return self.with_endpoint('api').request_get('node/fees', query)
