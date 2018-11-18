from client.exceptions import ArkParameterException
from client.resource import Resource


class Transactions(Resource):

    def get(self, transaction_id):
        return self.request_get('transactions/get', {'id': transaction_id})

    def all(self, limit=20, offset=None, **kwargs):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'limit': limit,
            'offset': offset,
            **extra_params
        }
        return self.request_get('transactions', params)

    def get_unconfirmed(self, transaction_id):
        return self.request_get('transactions/unconfirmed/get', {'id': transaction_id})

    def all_unconfirmed(self, limit=20, offset=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('transactions/unconfirmed', params)
