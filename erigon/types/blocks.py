import rlp
from eth.vm.forks.berlin.blocks import BerlinBlock
from eth.vm.forks.london.blocks import LondonBlock

Block = BerlinBlock | LondonBlock


def decode_block(data: bytes) -> Block:
    # identify sedes based on number of header fields
    sz = len(rlp.peek(data, 0, 0))
    if sz == 15:
        return rlp.decode(data, sedes=BerlinBlock)
    if sz == 16:
        return rlp.decode(data, sedes=LondonBlock)

    raise ValueError('invalid block')
