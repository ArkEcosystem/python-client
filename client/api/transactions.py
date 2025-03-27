from client.resource import Resource


class Transactions(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.with_endpoint('api').request_get('transactions', params)

    def create(self, transactions):
        return self.with_endpoint('transactions').request_post('transactions', data={'transactions': transactions})

    def get(self, transaction_id):
        return self.with_endpoint('api').request_get(f'transactions/{transaction_id}')

    def all_unconfirmed(self, limit=100, offset=None, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'limit': limit,
            'offset': offset,
            **extra_params
        }
        return self.with_endpoint('api').request_get('transactions/unconfirmed', params)

    def get_unconfirmed(self, transaction_id):
        return self.with_endpoint('api').request_get(f'transactions/unconfirmed/{transaction_id}')

    def configuration(self):
        return self.with_endpoint('transactions').request_get('configuration')
