from client.resource import Resource


class Commits(Resource):

    def get(self, height: int):
        return self.with_endpoint('api').request_get(f'commits/{height}')
