#!/usr/bin/env python

from park.builder.builder import Builder


class VoteBuilder(Builder):
    def create(secret, delegate, secondSecret=None):
        return self.build('vote.createVote', {
            "secret": secret,
            "delegate": delegate,
            "secondSecret": secondSecret
        })

    def delete(secret, delegate, secondSecret=None):
        return self.build('vote.deleteVote', {
            "secret": secret,
            "delegate": delegate,
            "secondSecret": secondSecret
        })
