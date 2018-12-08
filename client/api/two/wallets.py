from client.resource import Resource
from client.exceptions import ArkParameterException


class Wallets(Resource):

    def all(self, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('wallets', params)

    def top(self, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit
        }
        return self.request_get('wallets/top', params)

    def get(self, wallet_id):
        return self.request_get('wallets/{}'.format(wallet_id))

    def transactions(self, wallet_id, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('wallets/{}/transactions'.format(wallet_id), params)

    def transactions_sent(self, wallet_id, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('wallets/{}/transactions/sent'.format(wallet_id), params)

    def transactions_received(self, wallet_id, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('wallets/{}/transactions/received'.format(wallet_id), params)

    def votes(self, wallet_id, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('wallets/{}/votes'.format(wallet_id), params)

    def search(self, criteria, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('wallets/search', data=criteria, params=params)
