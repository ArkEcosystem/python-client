from client.resource import Resource


class Commits(Resource):

    def show(self, height):
        return self.with_endpoint('api').request_get(f'commits/{height}')
