
def pack_bits(bits: str) -> tuple[bytes, int]:
    if bits == "":
        return (b"", 0)
    
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