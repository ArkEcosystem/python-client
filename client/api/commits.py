from client.resource import Resource


class Commits(Resource):

    def show(self, block_number):
        return self.with_endpoint('api').request_get(f'commits/{block_number}')
