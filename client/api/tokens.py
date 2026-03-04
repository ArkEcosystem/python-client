from client.resource import Resource


class Tokens(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {k: v for k, v in kwargs.items() if v is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.with_endpoint('api').request_get('tokens', params)

    def all_with_whitelist(self, whitelist, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_post(
            'tokens', data={'whitelist': whitelist}, params=params
        )

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

    def transfers(self, address, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/transfers', params
        )

    def all_transfers(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(
            'tokens/transfers', params
        )

    def whitelist(self):
        return self.with_endpoint('api').request_get('tokens/whitelist')
