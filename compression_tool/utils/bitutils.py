""" Bit manipulation operations """

def pack_bits(bits: str) -> tuple[bytes, int]:
    """
    Convert a bitstring into packed bytes.

    The bitstream is padded with zero bits (if necessary) so its length is
    divisible by 8. Each group of 8 bits is then converted into the
    corresponding byte value.

    Args:
        bits: A string of '0' and '1' characters representing binary data.

    Returns:
        tuple:
            bytes: The packed bytes produced from the bitstring.
            pad_len: The number of zero bits added as padding (0-7).
    """
    if bits == "":
        return (b"", 0)
    if not set(bits).issubset({"0", "1"}):
        raise ValueError("bits must contain only '0' and '1'")
    
    n = len(bits)
    if n % 8 == 0:
        pad_len = 0
    else:
        pad_len = 8 - (n % 8)
    padded_bits = bits + "0" * pad_len
    chunks = [padded_bits[i: i + 8] for i in range(0,len(padded_bits), 8)]

    value_list = []
    for chunk in chunks:
        value = 0
        for bit in chunk:
            value <<= 1
            value += int(bit)
        value_list.append(value)
            
    return bytes(value_list), pad_len
    

def unpack_bits(data: bytes, pad_len: int) -> str:
    pass