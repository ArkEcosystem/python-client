from client.resource import Resource


class Commits(Resource):

    def show(self, height):
        return self.request_get(f'commits/{height}')
