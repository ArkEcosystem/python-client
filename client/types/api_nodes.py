from typing import TypedDict


ApiNodesQuery = TypedDict(
    'ApiNodesQuery',
    {
        'ip': str,
        'orderBy': str,
        'version': str,
    },
    total=False,
)
