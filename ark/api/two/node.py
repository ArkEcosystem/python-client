from ark.api.resource import Resource


class Node(Resource):

    def status(self):
        return self._request_get('node/status')

    def syncing(self):
        return self._request_get('node/syncing')

    def configuration(self):
        return self._request_get('node/configuration')
