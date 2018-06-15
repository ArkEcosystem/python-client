#!/usr/bin/env python

from park.one.api import API


class MultiSignature(API):
    def pending(self, publicKey):
        return self.get('api/'+self.client.api_version+'/multisignatures/pending',
                        {"publicKey": publicKey})

    def sign(self, transactionId, secret, parameters={}):
        return self.post('api/'+self.client.api_version+'/multisignatures/sign', {
            **{
                "transactionId": transactionId,
                "secret": secret
            },
            **parameters
        })

    def create(self, secret, secondSecret, keysgroup, lifetime, min):
        transaction = self.client.multiSignatureBuilder().create(
            secret, secondSecret, keysgroup, lifetime, min)

        return self.client.transport().createTransaction(transaction)

    def accounts(self, publicKey):
        return self.get('api/'+self.client.api_version+'/multisignatures/accounts',
                        {"publicKey": publicKey})
