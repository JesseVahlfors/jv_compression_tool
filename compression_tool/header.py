from typing import NamedTuple

class HeaderInfo(NamedTuple):
    version: str
    pad_len: int
    freq: dict[int, int]
    payload: str

NAME = "HUF"
VERSION = 1
FULL_VERSION = f"{NAME}{VERSION}"

def build_header(pad_len: int, freq: dict) -> str:
    pad = f"pad={pad_len}"
    

    freq_keys= sorted(freq.keys())
    freq_string = [f"{key}:{freq[key]}" for key in freq_keys]
    freq_string = "freq=" + ",".join(freq_string)

    header_list = [FULL_VERSION, pad, freq_string]
    header = "|".join(header_list) + "|"

    return header

def decode_header(data: str)-> HeaderInfo:
    if data.rfind("|") == -1:
        raise ValueError("Unknown header format")
    
    fields = data.split("|")

    version = fields[0]
    name = version[:3]
    version_num = int(version[3:])

    if name != NAME:
        raise ValueError("Unknown header format")
    if version_num > VERSION:
        raise ValueError("Unsupported newer version")

    pad_field = fields[1]
    if not pad_field.startswith("pad="):
        raise ValueError("pad field missing or malformed")
    
    pad_value = pad_field.split("=")[1]
    if pad_value == '':
        raise ValueError(f"pad length missing.")
    pad_len = int(pad_value)
    if 0 > pad_len or pad_len > 7:
        raise ValueError(f"pad length out of range: {pad_len}")

    freq_string_field = fields[2]
    if not freq_string_field.startswith("freq="):
        raise ValueError("freq field missing or malformed")
    freq_string = freq_string_field.split("=")[1]
    freq_string_list = freq_string.split(',')
    freq = {}
    for val in freq_string_list:
        val = val.split(':')
        freq[int(val[0])] = int(val[1])

    payload = fields[3]

    return HeaderInfo(version, pad_len, freq, payload)
    
 