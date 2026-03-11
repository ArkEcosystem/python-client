from client.resource import Resource


class ApiNodes(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get('api-nodes', query)
