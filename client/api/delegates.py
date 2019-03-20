from client.resource import Resource


class Delegates(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.request_get('delegates', params)

    def get(self, delegate_id):
        return self.request_get('delegates/{}'.format(delegate_id))

    def search(self, username, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('delegates/search', data={'username': username}, params=params)

    def blocks(self, delegate_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates/{}/blocks'.format(delegate_id), params)

    def voters(self, delegate_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('delegates/{}/voters'.format(delegate_id), params)
