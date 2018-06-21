from ark.resource import Resource


class Loader(Resource):
    def status(self):
        return self.request_get('loader/status')

    def sync(self):
        return self.request_get('loader/status/sync')

    def autoconfigure(self):
        return self.request_get('loader/autoconfigure')
