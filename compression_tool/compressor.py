# freq table from data -> build tree from freq table -> build code map from tree root ->
# for each byte lookup code in code map and concatenate into a codestring ->
# use pack_bits to turn codestring into bytes and get pad_len-> 
# use pad len and freq table to make header -> 
# return header + body bytes

from compression_tool import build_frequency_table, pack_bits, build_tree, build_code_map, build_header

def compress(data: bytes) -> bytes:
    pass


