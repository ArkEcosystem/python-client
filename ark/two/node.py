from ark.two.api import API


class Node(API):
    def status(self):
        return self.get('api/v2/node/status')

    def syncing(self):
        return self.get('api/v2/node/syncing')

    def configuration(self):
        return self.get('api/v2/node/configuration')
