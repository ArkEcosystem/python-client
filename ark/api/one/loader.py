from ark.api.resource import Resource


class Loader(Resource):
    def status(self):
        return self.request_get('api/loader/status')

    def sync(self):
        return self.request_get('api/loader/status/sync')

    def autoconfigure(self):
        return self.request_get('api/loader/autoconfigure')
