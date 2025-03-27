from client.resource import Resource


class Delegates(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.with_endpoint('api').request_get('delegates', params)

    def get(self, delegate_id):
        return self.with_endpoint('api').request_get(f'delegates/{delegate_id}')

    def blocks(self, delegate_id, **kwargs):
        return self.with_endpoint('api').request_get(f'delegates/{delegate_id}/blocks', kwargs)

    def voters(self, delegate_id, **kwargs):
        return self.with_endpoint('api').request_get(f'delegates/{delegate_id}/voters', kwargs)
