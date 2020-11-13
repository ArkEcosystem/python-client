from flatten_dict import flatten

class Resource(object):

    def __init__(self, connection):
        self.connection = connection

    def request_get(self, path, params=None):
        if params:
            params = flatten(params, reducer='dot')
        return self.connection.get(path, params=params)

    def request_post(self, path, data=None, params=None):
        if params:
            params = flatten(params, reducer='dot')
        return self.connection.post(path, data=data, params=params)
