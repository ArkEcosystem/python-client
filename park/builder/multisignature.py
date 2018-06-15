#!/usr/bin/env python

from park.builder.builder import Builder


class MultiSignatureBuilder(Builder):
    def create(secret, secondSecret, keysgroup, lifetime, min):
        return self.build('multisignature.createMultisignature', {
            "secret": secret,
            "secondSecret": secondSecret
        })
