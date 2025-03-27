from client.resource import Resource


class Votes(Resource):

    def all(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.with_endpoint('api').request_get('votes', params)

    def get(self, vote_id):
        return self.with_endpoint('api').request_get(f'votes/{vote_id}')
