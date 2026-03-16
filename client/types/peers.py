from typing import TypedDict


PeersQuery = TypedDict(
    'PeersQuery',
    {
        'page': int,
        'limit': int,
        'ip': str,
        'orderBy': str,
        'version': str,
    },
    total=False,
)
