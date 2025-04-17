from client.resource import Resource


class Validators(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.with_endpoint('api').request_get('validators', params)

    def get(self, validator_id):
        return self.with_endpoint('api').request_get(f'validators/{validator_id}')

    def blocks(self, validator_id, **kwargs):
        return self.with_endpoint('api').request_get(f'validators/{validator_id}/blocks', kwargs)

    def voters(self, validator_id, **kwargs):
        return self.with_endpoint('api').request_get(f'validators/{validator_id}/voters', kwargs)
