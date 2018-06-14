import os.path

import requests

from ark.exceptions import ArkHTTPException, ArkParameterException


class Connection(object):

    def __init__(self, hostname, api_version_number):
        if not isinstance(api_version_number, str) or api_version_number not in ['1', '2']:
            raise ArkParameterException('Only versions "1" and "2" are supported')

        self.session = requests.Session()
        self.hostname = hostname

        self.session.headers.update({
            'port': '1',
            'API-Version': api_version_number
        })

    def _build_url(self, path):
        return os.path.join(self.hostname, path)

    def _handle_response(self, response):
        if not response.content:
            raise ArkHTTPException('No content in response', response=response)

        body = response.json()
        if not response.ok:
            raise ArkHTTPException(
                '{} {} {} - {}'.format(
                    response.request.method,
                    response.status_code,
                    response.request.url,
                    body.get('error')
                ),
                response=response
            )

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
