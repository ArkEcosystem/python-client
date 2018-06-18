import logging
import os.path

import requests

logger = logging.getLogger(__name__)


class Connection(object):
    _nethash = None
    _version = None

    def __init__(self, client, host, port=None, nethash=None, version=None):
        self.session = requests.Session()

        self.host = host
        self.port = port
        self.nethash = nethash
        self.version = version
        self.client = client

        self.session.headers.update({
            'port': '1',
            'API-Version': self.client.api_version.replace('v', '')
        })

    @property
    def nethash(self):
        return self._nethash

    @nethash.setter
    def nethash(self, nethash):
        self._nethash = nethash
        if nethash:
            self.session.headers['nethash'] = nethash
        else:
            try:
                del self.session.headers['nethash']
            except KeyError:
                pass

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version
        if version:
            self.session.headers['version'] = version
        else:
            try:
                del self.session.headers['version']
            except KeyError:
                pass

    def _build_url(self, path):
        base_url = 'http://{}:{}/'.format(self.host, self.port)
        return os.path.join(base_url, path)

    def _handle_response(self, response):
        response.raise_for_status()

        body = response.json()

        if body['success'] is False:
            log_msg = '{} {} - {}'.format(
                response.request.method,
                response.request.url,
                body['error']
            )
            logger.error(log_msg)

        return body

    def get(self, path, params=None):
        url = self._build_url(path)
        response = self.session.get(url, params=params)
        return self._handle_response(response)

    def post(self, path, data=None, params=None):
        url = self._build_url(path)
        response = self.session.post(url, json=data, params=params)
        return self._handle_response(response)

    def put(self, path, data=None, params=None):
        url = self._build_url(path)
        response = self.session.put(url, json=data, params=params)
        return self._handle_response(response)

    def patch(self, path, data=None, params=None):
        url = self._build_url(path)
        response = self.session.patch(url, json=data, params=params)
        return self._handle_response(response)

    def delete(self, path, params=None):
        url = self._build_url(path)
        response = self.session.delete(url, params=params)
        return self._handle_response(response)

    def autoconfigure(self):
        if self.client.api_version == 'v1':
            loader_response = self.client.loader.autoconfigure()
            self.nethash = loader_response['network']['nethash']

            peer_response = self.client.peers.version()
            self.version = peer_response['version']
        else:
            config_response = self.client.node.configuration()
            self.nethash = config_response['data']['nethash']
            self.version = config_response['data']['version']
