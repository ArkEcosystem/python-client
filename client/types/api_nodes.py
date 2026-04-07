from typing import TypedDict


class ApiNodeResponse(TypedDict):
    url: str
    version: str
    height: int
    latency: int
    status: str


class ApiNodesQuery(TypedDict, total=False):
    ip: str
    orderBy: str
    version: str
