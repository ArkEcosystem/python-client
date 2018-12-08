from client.resource import Resource
from client.exceptions import ArkParameterException


class Delegates(Resource):

    def all(self, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates', params)

    def get(self, delegate_id):
        return self.request_get('delegates/{}'.format(delegate_id))

    def search(self, username, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('delegates/search', data={'username': username}, params=params)

    def blocks(self, delegate_id, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates/{}/blocks'.format(delegate_id), params)

    def voters(self, delegate_id, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates/{}/voters'.format(delegate_id), params)

    def voter_balances(self, delegate_id):
        return self.request_get('delegates/{}/voters/balances'.format(delegate_id))
