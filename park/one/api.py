#!/usr/bin/env python

from abc import ABC
import json
import requests


class API(ABC):
    def __init__(self, client):
        self.client = client

    def get(self, path, payload={}):
        return self.sendRequest('get', path, payload)

    def post(self, path, payload={}):
        return self.sendRequest('post', path, payload)

    def put(self, path, payload={}):
        return self.sendRequest('put', path, payload)

    def patch(self, path, payload={}):
        return self.sendRequest('patch', path, payload)

    def delete(self, path, payload={}):
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

        if (body['success'] == False):
            print(body['error'])

        return body

    def buildUrl(self, path):
        ip = self.client.ip
        port = self.client.port

        return f"http://{ip}:{port}/{path}"

    def buildHeaders(self):
        return {
            "nethash": self.client.nethash,
            "version": self.client.version,
            "port": "1"
        }
