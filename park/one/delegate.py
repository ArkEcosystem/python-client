#!/usr/bin/env python

from park.one.api import API


class Delegate(API):
    def __init__(self, client):
        self.client = client
        print(self.client.port)
    
    def count(self):
        return self.get('api/'+self.api_version+'/delegates/count')

    def search(self, query, parameters={}):
        return self.get('api/'+self.api_version+'/delegates/search', {**{"q": query}, **parameters})

    def voters(self, publicKey):
        return self.get('api/'+self.api_version+'/delegates/voters', {"publicKey": publicKey})

    def delegate(self, parameters={}):
        return self.get('api/'+self.api_version+'/delegates/get', parameters)

    def delegates(self, parameters={}):
        return self.get('api/'+self.api_version+'/delegates', parameters)

    def fee(self):
        return self.get('api/'+self.api_version+'/delegates/fee')

    def forgedByAccount(self, generatorPublicKey):
        return self.get('api/'+self.api_version+'/delegates/forging/getForgedByAccount',
                        {"generatorPublicKey": generatorPublicKey})

    def create(self, secret, username, secondSecret=None):
        transaction = self.client.delegateBuilder().create(
            secret, username, secondSecret)

        return self.client.transport().createTransaction(transaction)

    def nextForgers(self):
        return self.get('api/'+self.api_version+'/delegates/getNextForgers')

    def enableForging(self, secret, parameters={}):
        return self.post('api/'+self.api_version+'/delegates/forging/enable', {
            **{
                "secret": secret
            },
            **parameters
        })

    def disableForging(self, secret, parameters={}):
        return self.post('api/'+self.api_version+'/delegates/forging/disable', {
            **{
                "secret": secret
            },
            **parameters
        })

    def forgingStatus(self, publicKey, parameters={}):
        return self.get('api/'+self.api_version+'/delegates/forging/status', {
            **{
                "publicKey": publicKey
            },
            **parameters
        })
