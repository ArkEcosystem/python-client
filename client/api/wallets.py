from client.resource import Resource


class Wallets(Resource):

    def all(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get('wallets', params)

    def top(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit
        }
        return self.with_endpoint('api').request_get('wallets/top', params)

    def get(self, wallet_id):
        return self.with_endpoint('api').request_get(f'wallets/{wallet_id}')

    def transactions(self, wallet_id, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.with_endpoint('api').request_get(f'wallets/{wallet_id}/transactions', params)

    def transactions_sent(self, wallet_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(f'wallets/{wallet_id}/transactions/sent', params)

    def transactions_received(self, wallet_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(f'wallets/{wallet_id}/transactions/received', params)

    def votes(self, wallet_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get(f'wallets/{wallet_id}/votes', params)
