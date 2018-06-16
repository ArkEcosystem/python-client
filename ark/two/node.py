from ark.two.api import API


class Node(API):
    def status(self):
        return self.get('api/v2/node/status')

    def sync(self):
        return self.get('api/v2/node/syncing')

    def autoconfigure(self):
        return self.get('api/v2/node/configuration')
