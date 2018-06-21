import logging
import os.path

import requests

logger = logging.getLogger(__name__)


class Connection(object):

    def __init__(self, hostname, api_version_number):
        if not isinstance(api_version_number, str) or api_version_number not in ['1', '2']:
            raise Exception('Only versions "1" and "2" are supported')

        self.session = requests.Session()
        self.hostname = hostname

        self.session.headers.update({
            'port': '1',
            'API-Version': api_version_number
        })

    def _build_url(self, path):
        return os.path.join(self.hostname, path)

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
