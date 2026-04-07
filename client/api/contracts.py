from client.resource import Resource
from client.types import Response
from client.types.contracts import ContractAbiResponse, ContractResponse


class Contracts(Resource):

    def all(self) -> Response[ContractResponse]:
        return self.with_endpoint('api').request_get('contracts')

    def abi(self, name: str, implementation: str) -> Response[ContractAbiResponse]:
        return self.with_endpoint('api').request_get(f'contracts/{name}/{implementation}/abi')
