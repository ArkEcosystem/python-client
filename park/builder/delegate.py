#!/usr/bin/env python

from park.builder.builder import Builder


class DelegateBuilder(Builder):
    def create(secret, username, secondSecret):
        return self.build('delegate.createDelegate', {
            "secret": secret,
            "username": username,
            "secondSecret": secondSecret
        })
