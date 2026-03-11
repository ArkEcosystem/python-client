from client.resource import Resource


class Tokens(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get('tokens', query)

    def get(self, address):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}'
        )

    def holders(self, address, query={}):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/holders', query
        )

    def transfers_by_token(self, address, query={}):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/transfers', query
        )

    def transfers(self, query={}):
        return self.with_endpoint('api').request_get(
            'tokens/transfers', query
        )
