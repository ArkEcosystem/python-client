from typing import Literal, TypedDict


class ReceiptLog(TypedDict):
    data: str
    topics: list[str]
    address: str


class ReceiptResponse(TypedDict):
    transactionHash: str
    status: Literal[1, 0]
    gasUsed: int
    gasRefunded: int
    contractAddress: None
    logs: list[ReceiptLog]
    output: str


# Functional form required: keys include 'from' which is a reserved Python keyword
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


class ReceiptQuery(TypedDict, total=False):
    fullReceipt: bool
    includeTokens: bool


# Functional form required: keys include 'from' which is a reserved Python keyword
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
