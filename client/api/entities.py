from client.resource import Resource


class Entities(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.request_get('entities', params)

    def get(self, entity_id):
        return self.request_get('entities/{}'.format(entity_id))
