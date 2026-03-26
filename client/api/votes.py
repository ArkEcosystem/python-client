from typing import Optional

from client.resource import Resource
from client.types.votes import VoteQuery, VotesQuery


class Votes(Resource):

    def all(self, query: Optional[VotesQuery] = None):
        return self.with_endpoint('api').request_get('votes', query)

    def get(self, vote_id: str, query: Optional[VoteQuery] = None):
        return self.with_endpoint('api').request_get(f'votes/{vote_id}', query)
