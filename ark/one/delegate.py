#!/usr/bin/env python

from ark.one.api import API

class Delegate(API):

    def count(self):
        return self.get('api/delegates/count')

    def search(self, query, parameters={}):
        return self.get('api/delegates/search', {**{"q": query}, **parameters})

    def voters(self, publicKey):
        return self.get('api/delegates/voters', {"publicKey": publicKey})

    def delegate(self, parameters={}):
        '''
        :param publicKey: Unique public key for the delegate.
        :param username: Unique username for the delegate.
        :return: delegate
        '''

        return self.get('api/delegates/get', parameters)

    def delegates(self, parameters={}):
        '''
         :param offset: The offset of resources that will be returned.
         :param limit: The number of resources per page.
         :param orderBy: The column by which the resources will be sorted.
         :return: delegates
         '''

        return self.get('api/delegates', parameters)

    def fee(self):
        return self.get('api/delegates/fee')

    def forgedByAccount(self, generatorPublicKey):
        return self.get('api/delegates/forging/getForgedByAccount',
                        {"generatorPublicKey": generatorPublicKey})

    def create(self, transaction):
        return self.client.transport().createTransaction(transaction)

    def nextForgers(self):
        return self.get('api/delegates/getNextForgers')
