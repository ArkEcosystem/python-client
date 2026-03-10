from client.resource import Resource


class Wallets(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get('wallets', query)

    def top(self, query={}):
        return self.with_endpoint('api').request_get('wallets/top', query)

    def get(self, wallet_id):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}'
        )

    def transactions(self, wallet_id, query={}):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions', query
        )

    def sent_transactions(self, wallet_id, query={}):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions/sent', query
        )

    def received_transactions(self, wallet_id, query={}):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions/received', query
        )

    def votes(self, wallet_id, query={}):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/votes', query
        )

    def tokens(self, wallet_id, query={}):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/tokens', query
        )

    def tokens_for(self, query={}):
        return self.with_endpoint('api').request_get(
            'wallets/tokens', query
        )
