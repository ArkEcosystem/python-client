from client.resource import Resource


class Blocks(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.request_get('blocks', params)

    def get(self, block_id):
        return self.request_get('blocks/{}'.format(block_id))

    def transactions(self, block_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('blocks/{}/transactions'.format(block_id), params)

    def search(self, criteria, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('blocks/search', data=criteria, params=params)
