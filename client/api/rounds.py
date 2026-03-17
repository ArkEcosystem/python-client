from typing import Optional

from client.resource import Resource
from client.types import PaginatedQuery, PaginatedResponse, Response
from client.types.rounds import RoundResponse


class Rounds(Resource):

    def all(self, query: Optional[PaginatedQuery] = None) -> PaginatedResponse[RoundResponse]:
        return self.with_endpoint('api').request_get('rounds', query)

    def show(self, round_id: str) -> Response[RoundResponse]:
        return self.with_endpoint('api').request_get(f'rounds/{round_id}')

    def validators(self, round_id: str) -> Response[RoundResponse]:
        return self.with_endpoint('api').request_get(
            f'rounds/{round_id}/validators'
        )
