from client.resource import Resource


class ApiNodes(Resource):

    def all(self, **kwargs):
        return self.request_get('api-nodes', kwargs)
