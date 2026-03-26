from typing import List, TypedDict


TransactionsQuery = TypedDict(
    'TransactionsQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'address': str,
        'asset': str,
        'blockHash': str,
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
        'includeTokens': bool,
        'orderBy': str,
    },
    total=False,
)

UnconfirmedTransactionsQuery = TypedDict(
    'UnconfirmedTransactionsQuery',
    {
        'page': int,
        'limit': int,
        'orderBy': str,
    },
    total=False,
)

TransactionGetQuery = TypedDict(
    'TransactionGetQuery',
    {
        'fullReceipt': bool,
        'includeTokens': bool,
    },
    total=False,
)

TransactionCreateParams = TypedDict(
    'TransactionCreateParams',
    {
        'transactions': List[str],
    },
)
