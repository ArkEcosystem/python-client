
import backoff
import requests

from client.exceptions import ArkHTTPException, ArkParameterException


def giveup_handler(_):
    raise ArkHTTPException


# This uses the full_jitter algorithm
retry = backoff.on_exception(backoff.expo,
                             requests.exceptions.RequestException,
                             max_tries=3,
                             on_giveup=giveup_handler)


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
            request.url = '{}/{}'.format(self.hostname, request.url)
        return super().prepare_request(request)


class Connection(object):

    def __init__(self, hostname):
        self.hostname = hostname
        self.session  = Session(hostname=self.hostname)
        self.withEndpoint('api')

        self.session.headers.update({
            'Content-Type': 'application/json',
        })

    def withEndpoint(self, endpoint: str):
        """
        :param string endpoint: endpoint name
        """
        self.session.hostname = f'{self.hostname}/{endpoint}'

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
        response = self.session.get(path, params=params)
        return self._handle_response(response)

    def post(self, path, data=None, params=None):
        response = self.session.post(path, json=data, params=params)
        return self._handle_response(response)
