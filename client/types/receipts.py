from typing import TypedDict


ReceiptsQuery = TypedDict(
    'ReceiptsQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'from': str,
        'to': str,
        'fullReceipt': bool,
        'includeTokens': bool,
        'transactionHash': str,
    },
    total=False,
)

ReceiptQuery = TypedDict(
    'ReceiptQuery',
    {
        'fullReceipt': bool,
        'includeTokens': bool,
    },
    total=False,
)

ReceiptContractsQuery = TypedDict(
    'ReceiptContractsQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'from': str,
        'fullReceipt': bool,
        'includeTokens': bool,
    },
    total=False,
)
