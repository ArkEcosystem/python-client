from typing import Optional

from client.resource import Resource
from client.types import PaginatedResponse, Response
from client.types.transactions import TransactionResponse
from client.types.votes import VoteQuery, VotesQuery


class Votes(Resource):

    def all(self, query: Optional[VotesQuery] = None) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get('votes', query)

    def get(self, vote_id: str, query: Optional[VoteQuery] = None) -> Response[TransactionResponse]:
        return self.with_endpoint('api').request_get(f'votes/{vote_id}', query)
