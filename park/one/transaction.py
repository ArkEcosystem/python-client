#!/usr/bin/env python

from park.one.api import API

class Transaction(API):
    def transaction(self, id):
        return self.get('api/transactions/get', {"id": id})

    def transactions(self, parameters={}):
        return self.get('api/transactions', parameters)

    # TO FIX - BOTH UNCONFIRMED TRANSACTION FUNCTIONS SEEM BROKEN
    def unconfirmedTransaction(self, id):
        return self.get('api/transactions/unconfirmed/get', {"id": id})

    def unconfirmedTransactions(self, parameters={}):
        return self.get('api/transactions/unconfirmed', parameters)

    def create(self, transaction):
        return self.client.transport().createTransaction(transaction)
