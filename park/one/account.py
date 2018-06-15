#!/usr/bin/env python

from park.one.api import API

class Account(API):
    def balance(self, address):
        return self.get('api/accounts/getBalance', {"address": address})

    def publickey(self, address):
        return self.get('api/accounts/getPublicKey', {"address": address})

    def delegates(self, address):
        return self.get('api/accounts/delegates', {"address": address})

    def delegatesFee(self):
        return self.get('api/accounts/delegates/fee')

    def account(self, address):
        return self.get('api/accounts', {"address": address})

    def accounts(self, parameters={}):
        return self.get('api/accounts/getAllAccounts', parameters)

    def top(self, parameters={}):
        return self.get('api/accounts/top', parameters)

    def count(self):
        return self.get('api/accounts/count')
