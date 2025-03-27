from typing import Any
from client.resource import Resource


class EVM(Resource):
    def eth_call(self, params: list[dict[str, Any]]):
        return self.with_endpoint('evm').request_post('', {
            'jsonrpc': "2.0",
            'method': "eth_call",
            'params': [params, "latest"],
            'id': None,
        })
