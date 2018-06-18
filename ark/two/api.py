import requests


class API():
    def __init__(self, client):
        self.client = client

    def get(self, path, payload=None):
        return self.send_request('get', path, payload)

    def post(self, path, payload=None):
        return self.send_request('post', path, payload)

    def put(self, path, payload=None):
        return self.send_request('put', path, payload)

    def patch(self, path, payload=None):
        return self.send_request('patch', path, payload)

    def delete(self, path, payload=None):
        return self.send_request('delete', path, payload)

    def send_request(self, method, path, payload):
        url = self.build_url(path)

        if method in ['get', 'delete']:
            response = getattr(requests, method)(
                url, headers=self.build_headers(), params=payload)
        else:
            response = getattr(requests, method)(
                url, headers=self.build_headers(), json=payload)

        body = response.json()

        return body

    def build_url(self, path):
        ip = self.client.ip
        port = self.client.port

        return 'http://{}:{}/{}'.format(ip, port, path)

    def build_headers(self):
        return {
            'nethash': self.client.nethash,
            'version': self.client.version,
            'port': '1'
        }
