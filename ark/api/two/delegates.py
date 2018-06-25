from ark.resource import Resource


class Delegates(Resource):

    def all(self, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates', params)

    def get(self, delegate_id):
        return self.request_get('delegates/{}'.format(delegate_id))

    def search(self, criteria, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('delegates/search'.format(), data=criteria, params=params)

    def blocks(self, delegate_id, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates/{}/blocks'.format(delegate_id), params)

    def voters(self, delegate_id, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates/{}/voters'.format(delegate_id), params)

    def voter_balances(self, delegate_id):
        return self.request_get('delegates/{}/voterBalances'.format(delegate_id))
