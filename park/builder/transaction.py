#!/usr/bin/env python

from park.builder.builder import Builder


class TransactionBuilder(Builder):
    def create(self,
               recipientId,
               amount,
               vendorField,
               secret,
               secondSecret=None):
        return self.build(
            'transaction.createTransaction', {
                "recipientId": recipientId,
                "amount": amount,
                "vendorField": vendorField,
                "secret": secret,
                "secondSecret": secondSecret
            })
