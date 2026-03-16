from typing import Optional

from client.resource import Resource
from client.types.api_nodes import ApiNodesQuery


class ApiNodes(Resource):

    def all(self, query: Optional[ApiNodesQuery] = None):
        return self.with_endpoint('api').request_get('api-nodes', query)
