#!/usr/bin/env python

from abc import ABC
from Naked.toolshed.shell import muterun_js
from jinja2 import Environment, FileSystemLoader
import sys
import json
import os


class Builder(ABC):
    def __init__(self, client):
        self.client = client
        self.env = Environment(
            loader=FileSystemLoader(
                os.path.join(os.path.dirname(__file__), 'templates')))

    def build(self, script, data):
        network = {
            '6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988':
            {
                "netPubKey": "0x17",
                'js': 'arkjs'
            },  # ark mainnet
            '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23':
            {
                "netPubKey": "0x1E",
                'js': 'arkjs'
            },  # ark devnet
        }[self.client.nethash]

        template = self.env.get_template(script + ".py").render({
            **{
                "network": network['netPubKey'],
                "javascript": network['js']
            },
            **data
        })

        transactionScript = script + ".js"

        with open(transactionScript, "wt") as fh:
            fh.write(template)

        response = muterun_js(transactionScript)

        if response.exitcode == 0:
            os.remove(transactionScript)

            return json.loads(response.stdout.decode('utf-8'))
        else:
            sys.stderr.write(response.stderr.decode('utf-8'))
