
from typing import Literal, Optional, TypedDict
import backoff
import requests

from client.exceptions import ArkHTTPException


def giveup_handler(_):
    raise ArkHTTPException


# This uses the full_jitter algorithm
retry = backoff.on_exception(backoff.expo,
                             requests.exceptions.RequestException,
                             max_tries=3,
                             on_giveup=giveup_handler)


class ClientHosts(TypedDict):
    api: str
    transactions: Optional[str]
    evm: Optional[str]

class Session(requests.Session):

    def __init__(self, *args, **kwargs):
        if 'hostname' in kwargs:
            self.hostname = kwargs.pop('hostname')
        super().__init__(*args, **kwargs)

    @retry
    def send(self, request, **kwargs):
        kwargs.update({
            'timeout': (1, 5)
        })
        return super().send(request, **kwargs)

    def prepare_request(self, request):
        if self.hostname is not None:
            request.url = f'{self.hostname}/{request.url}'
        return super().prepare_request(request)

class Connection(object):
    session: Session
    hosts: ClientHosts

    def __init__(self, hosts: str | ClientHosts):
        if isinstance(hosts, str):
            hosts = {
                'api': hosts,
                'transactions': None,
                'evm': None,
            }

        self.hosts = hosts

        # Ensure we have a session
        self.with_endpoint('api')

    def with_endpoint(self, endpoint: Literal['api', 'transactions', 'evm']):
        """
        :param string endpoint: endpoint name
        """
        host = self.hosts[endpoint]
        if host is None:
            host = self.hosts['api']

        self.session = Session(hostname=f'{host}')

        self.session.headers.update({
            'Content-Type': 'application/json',
        })

    def _handle_response(self, response: requests.Response):
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
        response = self.session.get(path, params=params)

        return self._handle_response(response)

    def post(self, path, data=None, params=None):
        response = self.session.post(path, json=data, params=params)

        return self._handle_response(response)
