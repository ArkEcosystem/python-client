from typing import TypedDict


class CommitResponse(TypedDict):
    blockNumber: str
    signature: str
    validators: list[str]
