from typing import NamedTuple

NAME = "HUF"
VERSION = 1
FULL_VERSION = f"{NAME}{VERSION}"

class HeaderInfo(NamedTuple):
    version: str
    pad_len: int
    freq: dict[int, int]
    payload: str

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
    
    header_fields, payload = _split_header_and_payload(data)
    version = header_fields[0]
    pad_field = header_fields[1]
    freq_string_field = header_fields[2]

    version = _parse_version(version)
    pad_len = _parse_pad(pad_field)
    freq = _parse_freq(freq_string_field)

    return HeaderInfo(version, pad_len, freq, payload)
    
def _split_header_and_payload(data: str) -> tuple[list[str], str]:
    payload_idx = data.rfind("|")
    header = data[:payload_idx]
    payload = data[payload_idx +1 :]

    fields = header.split("|")
    if len(fields) < 3:
        raise ValueError("Unknown header format")
    return fields, payload

def _parse_version(version):
    if len(version) < 4: 
        raise ValueError("Unknown version format")
    
    name = version[:3]
    suffix = version[3:]

    if not suffix.isdigit():
        raise ValueError("Unknown version format")
    
    version_num = int(suffix)
    if name != NAME:
        raise ValueError("Unknown header format")
    if version_num > VERSION:
        raise ValueError("Unsupported newer version")
    return version
    
def _parse_pad(pad_field: str) -> int:
    if not pad_field.startswith("pad="):
        raise ValueError("pad field missing or malformed")
    pad_value = pad_field.split("=")[1]
    if pad_value == '':
        raise ValueError(f"pad length missing.")
    pad_len = int(pad_value)
    if 0 > pad_len or pad_len > 7:
        raise ValueError(f"pad length out of range: {pad_len}")
    return pad_len

def _parse_freq(freq_string_field: str) -> dict[int, int]:
    freq = {}
    if not freq_string_field.startswith("freq="):
        raise ValueError("freq field missing or malformed")
    freq_string = freq_string_field.split("=")[1]
    if freq_string == "":
        return {}
    freq_string_list = freq_string.split(',')
    for val in freq_string_list:
        val = val.split(':')
        if len(val) != 2:
            raise ValueError("symbol or weight missing")
        symbol = int(val[0])
        weight = int(val[1])
        if 255 < symbol or symbol < 0 or weight < 1:
            raise ValueError(f"symbol must be 0-255 and weight >= 1")
        if symbol in freq:
            raise ValueError(f"Symbol duplicate in freq dict")
        freq[symbol] = int(weight)
    return freq
    
    
    
 