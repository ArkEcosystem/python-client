from typing import TypedDict


BlocksQuery = TypedDict(
    'BlocksQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'transform': bool,
        'orderBy': str,
        'id': str,
        'number': int,
        'height.from': int,
        'height.to': int,
        'timestamp': int,
        'timestamp.from': int,
        'timestamp.to': int,
    },
    total=False,
)

BlockTransactionsQuery = TypedDict(
    'BlockTransactionsQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'orderBy': str,
    },
    total=False,
)
