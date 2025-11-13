""" pad_len = 3
freq = {97: 4, 98: 5, 99: 1}
"HUF1|pad=3|freq=97:4,98:5,99:1|" """
from typing import NamedTuple

def build_header(pad_len: int, freq: dict) -> str:
    version = "HUF1"
    pad = f"pad={pad_len}"
    

    freq_keys= sorted(freq.keys())
    freq_string = [f"{key}:{freq[key]}" for key in freq_keys]
    freq_string = "freq=" + ",".join(freq_string)

    header_list = [version, pad, freq_string]
    header = "|".join(header_list) + "|"

    return header

def decode_header(header: str)-> NamedTuple:
    return None
 