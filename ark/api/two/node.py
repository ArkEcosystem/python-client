from ark.resource import Resource


class Node(Resource):

    def status(self):
        return self.request_get('node/status')

    def syncing(self):
        return self.request_get('node/syncing')

    def configuration(self):
        return self.request_get('node/configuration')
