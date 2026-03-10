from client.resource import Resource


class Transactions(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get(
            'transactions', query
        )

    def create(self, transactions):
        return self.with_endpoint('transactions').request_post(
            'transactions', data={'transactions': transactions}
        )

    def get(self, transaction_id):
        return self.with_endpoint('api').request_get(
            f'transactions/{transaction_id}'
        )

    def all_unconfirmed(self, query={}):
        return self.with_endpoint('api').request_get(
            'transactions/unconfirmed', query
        )

    def get_unconfirmed(self, transaction_id):
        return self.with_endpoint('api').request_get(
            f'transactions/unconfirmed/{transaction_id}'
        )

    def configuration(self):
        return self.with_endpoint('transactions').request_get(
            'configuration'
        )
