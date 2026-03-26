from typing import Optional

from client.resource import Resource
from client.types.node import NodeFeesQuery


class Node(Resource):

    def status(self):
        return self.with_endpoint('api').request_get('node/status')

    def syncing(self):
        return self.with_endpoint('api').request_get('node/syncing')

    def configuration(self):
        return self.with_endpoint('api').request_get(
            'node/configuration'
        )

    def crypto(self):
        return self.with_endpoint('api').request_get(
            'node/configuration/crypto'
        )

    def fees(self, query: Optional[NodeFeesQuery] = None):
        return self.with_endpoint('api').request_get('node/fees', query)
