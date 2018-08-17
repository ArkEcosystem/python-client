from ark.resource import Resource


class Transactions(Resource):

    def all(self, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('transactions', params)

    def create(self, transactions):
        return self.request_post('transactions', data={'transactions': transactions})

    def get(self, transaction_id):
        return self.request_get('transactions/{}'.format(transaction_id))

    def all_unconfirmed(self, limit=20, offset=None):
        params = {
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('transactions/unconfirmed', params)

    def get_unconfirmed(self, transaction_id):
        return self.request_get('transactions/unconfirmed/{}'.format(transaction_id))

    def search(self, criteria, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('transactions/search', data=criteria, params=params)

    def types(self):
        return self.request_get('transactions/types')

    def fees(self):
        return self.request_get('transactions/fees')
