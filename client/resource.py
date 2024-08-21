from typing import Literal
from flatten_dict import flatten

from client.connection import Connection

class Resource(object):

    def __init__(self, connection: Connection):
        self.connection = connection

    def with_endpoint(self, endpoint: Literal['api', 'transactions', 'evm']):
        self.connection.with_endpoint(endpoint)
        return self

    def request_get(self, path, params=None):
        if params:
            params = flatten(params, reducer='dot')
        return self.connection.get(path, params=params)

    def request_post(self, path, data=None, params=None):
        if params:
            params = flatten(params, reducer='dot')
        return self.connection.post(path, data=data, params=params)
