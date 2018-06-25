from ark.resource import Resource


class Votes(Resource):

    def all(self, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('votes', params)

    def get(self, vote_id):
        return self.request_get('votes/{}'.format(vote_id))
