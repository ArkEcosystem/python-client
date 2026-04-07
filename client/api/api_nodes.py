from typing import Optional

from client.resource import Resource
from client.types import PaginatedResponse
from client.types.api_nodes import ApiNodeResponse, ApiNodesQuery


class ApiNodes(Resource):

    def all(self, query: Optional[ApiNodesQuery] = None) -> PaginatedResponse[ApiNodeResponse]:
        return self.with_endpoint('api').request_get('api-nodes', query)
