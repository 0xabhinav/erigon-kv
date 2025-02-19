# erigon uses an accursed encoding for hash types
# ported from https://github.com/ledgerwatch/erigon-lib/blob/main/gointerfaces/type_utils.go
from typing import Any
from erigon.proto.types.types_pb2 import H128, H160, H256, H512, H1024, H2048

HashType = Any
HASH_TYPES = {16: H128, 20: H160, 32: H256, 64: H512, 128: H1024, 256: H2048}


def to_bytes(number: int, size: int = 8):
    return number.to_bytes(size, "big")


def to_int(data: bytes):
    return int.from_bytes(data, "big")


def decode_hash(msg: HashType) -> bytes:
    if msg == H128():
        return to_bytes(msg.hi) + to_bytes(msg.lo)
    if msg == H160():
        return decode_hash(msg.hi) + to_bytes(msg.lo, 4)
    if msg in (H256(), H512(),  H1024(), H2048()):
        return decode_hash(msg.hi) + decode_hash(msg.lo)

    raise TypeError("unsupported type %s", type(msg))


def encode_hash(data: bytes) -> HashType:
    if len(data) == 16:
        return H128(hi=to_int(data[:8]), lo=to_int(data[8:]))
    if len(data) == 20:
        return H160(hi=encode_hash(data[:16]), lo=to_int(data[16:20]))
    if len(data) in [32, 64, 128, 256]:
        size = len(data)
        half = size // 2
        return HASH_TYPES[size](hi=encode_hash(data[:half]), lo=encode_hash(data[half:]))

    raise ValueError("invalid data length %d", len(data))
