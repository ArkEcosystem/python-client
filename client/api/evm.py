from client.resource import Resource
from client.types.evm import EvmBodyPartialParams


class EVM(Resource):
    def call(self, payload: EvmBodyPartialParams):
        return self.with_endpoint('evm').request_post('', {
            'jsonrpc': "2.0",
            **payload,
        })
