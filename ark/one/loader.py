from ark.one.api import API


class Loader(API):
    def status(self):
        return self.get('api/loader/status')

    def sync(self):
        return self.get('api/loader/status/sync')

    def autoconfigure(self):
        return self.get('api/loader/autoconfigure')
