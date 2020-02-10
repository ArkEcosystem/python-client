from client.resource import Resource


class Businesses(Resource):

    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'page': page,
            'limit': limit,
            **extra_params
        }
        return self.request_get('businesses', params)

    def get(self, business_id):
        return self.request_get('businesses/{}'.format(business_id))

    def bridgechains(self, business_id, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit
        }
        return self.request_get('businesses/{}/bridgechains'.format(business_id), params)

    def search(self, criteria, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_post('businesses/search', data=criteria, params=params)
