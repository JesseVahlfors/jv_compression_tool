from typing import NamedTuple

class HeaderInfo(NamedTuple):
    version: str
    pad_len: int
    freq: dict[int, int]
    payload: str

def build_header(pad_len: int, freq: dict) -> str:
    version = "HUF1"
    pad = f"pad={pad_len}"
    

    freq_keys= sorted(freq.keys())
    freq_string = [f"{key}:{freq[key]}" for key in freq_keys]
    freq_string = "freq=" + ",".join(freq_string)

    header_list = [version, pad, freq_string]
    header = "|".join(header_list) + "|"

    return header

def decode_header(data: str)-> HeaderInfo:
    payload_idx = data.rfind("|")
    header = data[:payload_idx]
    payload = data[payload_idx + 1:]

    fields = header.split("|")

    version = fields[0]

    pad_field = fields[1]
    pad_value = pad_field[pad_field.rfind("=") +1:]
    pad_len = int(pad_value)

    freq_string_field = fields[2]
    freq_string = freq_string_field[freq_string_field.rfind("=") +1:]
    freq_string_list = freq_string.split(',')
    freq = {}
    for val in freq_string_list:
        val = val.split(':')
        freq[int(val[0])] = int(val[1])

    return HeaderInfo(version, pad_len, freq, payload)
    
 