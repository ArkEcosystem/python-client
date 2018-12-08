from client.resource import Resource
from client.exceptions import ArkParameterException

class Votes(Resource):

    def all(self, page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('votes', params)

    def get(self, vote_id):
        return self.request_get('votes/{}'.format(vote_id))
