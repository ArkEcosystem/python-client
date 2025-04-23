from client.resource import Resource


class Contracts(Resource):

    def all(self):
        return self.with_endpoint('api').request_get('contracts')

    def abi(self, name: str, implementation: str):
        return self.with_endpoint('api').request_get(f'contracts/{name}/{implementation}/abi')
