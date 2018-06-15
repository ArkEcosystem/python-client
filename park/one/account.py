#!/usr/bin/env python

from park.one.api import API

class Account(API):
    def balance(self, address):
        return self.get('api/'+self.client.api_version+'/accounts/getBalance', {"address": address})

    def publickey(self, address):
        return self.get('api/'+self.client.api_version+'/accounts/getPublicKey', {"address": address})

    def delegates(self, address):
        return self.get('api/'+self.client.api_version+'/accounts/delegates', {"address": address})

    '''
    def delegatesFee(self, address):
        return self.get('api/'+self.client.api_version+'/accounts/delegates/fee', {"address": address})
    '''

    def delegatesFee(self):
        return self.get('api/' + self.client.api_version + '/accounts/delegates/fee')

    def vote(self, secret, publicKey, secondSecret):
        return self.put('api/'+self.client.api_version+'/accounts/delegates', {
            "secret": secret,
            "publicKey": publicKey,
            "secondSecret": secondSecret
        })

    def account(self, address):
        return self.get('api/'+self.client.api_version+'/accounts', {"address": address})

    def accounts(self, parameters={}):
        return self.get('api/'+self.client.api_version+'/accounts/getAllAccounts', parameters)

    def top(self, parameters={}):
        return self.get('api/'+self.client.api_version+'/accounts/top', parameters)

    def count(self):
        return self.get('api/'+self.client.api_version+'/accounts/count')
