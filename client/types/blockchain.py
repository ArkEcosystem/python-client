from typing import TypedDict


class BlockchainBlock(TypedDict):
    hash: str
    number: int


class BlockchainResponse(TypedDict):
    block: BlockchainBlock
    supply: str
