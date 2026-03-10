from client.resource import Resource


class Tokens(Resource):

    def all(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get('tokens', params)

    def get(self, address):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}'
        )

    def holders(self, address, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/holders', params
        )

    def transfers_by_token(self, address, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/transfers', params
        )

    def transfers(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(
            'tokens/transfers', params
        )
