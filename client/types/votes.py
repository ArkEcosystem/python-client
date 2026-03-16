from typing import TypedDict


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

VoteQuery = TypedDict(
    'VoteQuery',
    {
        'fullReceipt': bool,
    },
    total=False,
)
