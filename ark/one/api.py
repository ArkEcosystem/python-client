from abc import ABC
import logging

import requests


logger = logging.getLogger(__name__)


class API(ABC):
    def __init__(self, client):
        self.client = client

    def get(self, path, payload=None):
        return self.sendRequest('get', path, payload)

    def post(self, path, payload=None):
        return self.sendRequest('post', path, payload)

    def put(self, path, payload=None):
        return self.sendRequest('put', path, payload)

    def patch(self, path, payload=None):
        return self.sendRequest('patch', path, payload)

    def delete(self, path, payload=None):
        return self.sendRequest('delete', path, payload)

    def sendRequest(self, method, path, payload):
        url = self.buildUrl(path)

        if method in ['get', 'delete']:
            response = getattr(requests, method)(
                url, headers=self.buildHeaders(), params=payload)
        else:
            response = getattr(requests, method)(
                url, headers=self.buildHeaders(), json=payload)

        body = response.json()

        if body['success'] is False:
            log_msg = '{} {} - {}'.format(method.upper(), path, body['error'])
            logger.error(log_msg)

        return body

    def buildUrl(self, path):
        ip = self.client.ip
        port = self.client.port

        return 'http://{}:{}/{}'.format(ip, port, path)

    def buildHeaders(self):
        return {
            'nethash': self.client.nethash,
            'version': self.client.version,
            'port': '1'
        }
