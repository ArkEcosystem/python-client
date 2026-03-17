from client.resource import Resource
from client.types import Response
from client.types.commits import CommitResponse


class Commits(Resource):

    def get(self, height: int) -> Response[CommitResponse]:
        return self.with_endpoint('api').request_get(f'commits/{height}')
