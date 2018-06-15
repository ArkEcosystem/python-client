#!/usr/bin/env python

from park.builder.builder import Builder


class SignatureBuilder(Builder):
    def create(secret, secondSecret):
        return self.build('signature.createSignature', {
            "secret": secret,
            "secondSecret": secondSecret
        })
