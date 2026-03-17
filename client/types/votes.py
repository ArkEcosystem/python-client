from typing import TypedDict


# Functional form required: keys include 'from' which is a reserved Python keyword
VotesQuery = TypedDict(
    'VotesQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'address': str,
        'blockHash': str,
        'data': str,
        'from': str,
        'gasPrice': int,
        'hash': str,
        'nonce': int,
        'senderId': str,
        'senderPublicKey': str,
        'timestamp': int,
        'to': str,
        'transactionIndex': int,
        'value': int,
        'fullReceipt': bool,
        'orderBy': str,
    },
    total=False,
)


class VoteQuery(TypedDict, total=False):
    fullReceipt: bool
