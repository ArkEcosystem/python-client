from client.resource import Resource
from client.types import Response
from client.types.blockchain import BlockchainResponse


class Blockchain(Resource):

    def blockchain(self) -> Response[BlockchainResponse]:
        return self.with_endpoint('api').request_get('blockchain')
