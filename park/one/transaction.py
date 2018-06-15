#!/usr/bin/env python

from park.one.api import API


class Transaction(API):
    def transaction(self, id):
        return self.get('api/'+self.client.api_version+'/transactions/get', {"id": id})

    def transactions(self, parameters={}):
        return self.get('api/'+self.client.api_version+'/transactions', parameters)

    def unconfirmedTransaction(self, id):
        return self.get('api/'+self.client.api_version+'/transactions/unconfirmed/get', {"id": id})

    def unconfirmedTransactions(self, parameters={}):
        return self.get('api/'+self.client.api_version+'/transactions/unconfirmed', parameters)

    def create(self,
               recipientId,
               amount,
               vendorField,
               secret,
               secondSecret=None):
        transaction = self.client.transactionBuilder().create(
            recipientId, amount, vendorField, secret, secondSecret)

        return self.client.transport().createTransaction(transaction)
