from client.resource import Resource


class Locks(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.request_get('locks', params)

    def get(self, lock_id):
        return self.request_get('locks/{}'.format(lock_id))

    def search(self, criteria, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('locks/search', data=criteria, params=params)

    def unlocked(self, criteria, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('locks/unlocked', data=criteria, params=params)
