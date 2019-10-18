from client.resource import Resource


class Bridgechains(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.request_get('bridgechains', params)

    def get(self, bridgechain_id):
        return self.request_get('bridgechains/{}'.format(bridgechain_id))

    def search(self, criteria, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('bridgechains/search', data=criteria, params=params)
