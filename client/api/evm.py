from typing import Any
from client.resource import Resource


class EVM(Resource):
    def call(self, params: dict[str, Any]):
        return self.with_endpoint('evm').request_post('', {
            'jsonrpc': "2.0",
            **params,
        })
