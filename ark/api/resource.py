
class Resource(object):

    def __init__(self, connection):
        self.connection = connection

    def _request_get(self, path, params=None):
        return self.connection.get(path, params=params)

    def _request_post(self, path, data=None, params=None):
        return self.connection.post(path, data=data, params=params)

    def _request_put(self, path, data=None, params=None):
        return self.connection.put(path, data=data, params=params)

    def _request_patch(self, path, data=None, params=None):
        return self.connection.patch(path, data=data, params=params)

    def _request_delete(self, path, params=None):
        return self.connection.delete(path, params=params)
