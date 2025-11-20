# freq table from data -> build tree from freq table -> build code map from tree root ->
# for each byte lookup code in code map and concatenate into a codestring ->
# use pack_bits to turn codestring into bytes and get pad_len-> 
# use pad len and freq table to make header -> 
# return header + body bytes
from compression_tool.header import build_header
from compression_tool.frequency import build_frequency_table
from compression_tool.build_tree import build_tree
from compression_tool.code_map import build_code_map
from compression_tool.utils.bitutils import pack_bits


def compress(data: bytes) -> bytes:
    if data == b"":
        return build_header(0, {})
    
    freq_table = build_frequency_table(data)
    root = build_tree(freq_table)
    code_map = build_code_map(root)
    codestring = ""
    for symbol in data:
        codestring += code_map[symbol]
    packed_bytes, pad_len = pack_bits(codestring)
    header = build_header(pad_len, freq_table)
    header_bytes = header.encode("utf-8")

    return header_bytes + packed_bytes
