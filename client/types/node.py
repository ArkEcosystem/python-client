from typing import TypedDict

from typing_extensions import NotRequired

from client.types.blocks import Block


class NodeStatusResponse(TypedDict):
    blocksCount: int
    now: int
    synced: bool
    timestamp: int


class NodeSyncingResponse(TypedDict):
    blocks: int
    blockNumber: int
    id: int
    syncing: bool


class NodeConfigurationTransactionPoolDynamicFees(TypedDict):
    enabled: bool


class NodeConfigurationTransactionPool(TypedDict):
    dynamicFees: NodeConfigurationTransactionPoolDynamicFees


class NodeConfigurationCore(TypedDict):
    version: str


class NativeGasLimits(TypedDict, total=False):
    vote: int
    transfer: int
    multiPayment: int
    multiSignature: int
    usernameResignation: int
    usernameRegistration: int
    validatorResignation: int
    validatorRegistration: int


class ConstantGas(TypedDict, total=False):
    minimumGasFee: int
    maximumGasLimit: int
    minimumGasLimit: int
    nativeGasLimits: NativeGasLimits
    nativeFeeMultiplier: int


class StaticFees(TypedDict, total=False):
    vote: int
    transfer: int
    multiPayment: int
    multiSignature: int
    usernameResignation: int
    usernameRegistration: int
    validatorResignation: int
    validatorRegistration: int


class ConstantFees(TypedDict, total=False):
    staticFees: StaticFees


class ConstantBlock(TypedDict, total=False):
    version: int
    maxPayload: int
    maxGasLimit: int
    maxTransactions: int


class ConstantAddress(TypedDict, total=False):
    keccak256: bool


class ConstantSatoshi(TypedDict, total=False):
    decimals: int
    denomination: int


class ConfigurationTimeouts(TypedDict):
    blockTime: int
    tolerance: int
    stageTimeout: int
    blockPrepareTime: int
    stageTimeoutIncrease: int


class Constant(TypedDict, total=False):
    gas: ConstantGas
    fees: ConstantFees
    block: ConstantBlock
    epoch: str
    height: int
    reward: str
    address: ConstantAddress
    evmSpec: str
    satoshi: ConstantSatoshi
    timeouts: ConfigurationTimeouts
    activeValidators: int
    multiPaymentLimit: int
    vendorFieldLength: int


class NodeConfigurationResponse(TypedDict):
    constants: Constant
    core: NodeConfigurationCore
    explorer: str
    nethash: str
    ports: dict[str, int]
    slip44: int
    symbol: str
    token: str
    transactionPool: NodeConfigurationTransactionPool
    version: int
    wif: int


class NetworkClient(TypedDict):
    token: str
    symbol: str
    explorer: str


class Network(TypedDict):
    wif: int
    name: str
    client: NetworkClient
    slip44: int
    chainId: int
    nethash: str
    pubKeyHash: int
    messagePrefix: str


class GenesisBlockProof(TypedDict):
    round: int
    signature: str
    validators: list


class GenesisBlock(TypedDict):
    block: Block
    proof: GenesisBlockProof
    serialized: str


class NodeCryptoResponse(TypedDict):
    network: Network
    milestones: list[Constant]
    genesisBlock: GenesisBlock


class TransactionTypeFee(TypedDict):
    avg: str
    max: str
    min: str
    sum: str


NodeFeesResponse = dict[str, TransactionTypeFee]


class NodeFeesQuery(TypedDict, total=False):
    days: int
