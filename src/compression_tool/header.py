"""
Header encoding/decoding for the Huffman compression tool.

This module defines:
- build_header(...)
- decode_header(...)
- HeaderInfo result type
- Internal helper parsing functions
"""
from typing import NamedTuple

NAME = "HUF"
VERSION = 1
FULL_VERSION = f"{NAME}{VERSION}"

class HeaderInfo(NamedTuple):
    """Parsed header information returned by decode_header()."""
    version: str
    pad_len: int
    freq: dict[int, int]

def build_header(pad_len: int, freq: dict[int, int]) -> str:
    """
    Build the header string for a compressed Huffman file.

    Format:
        HUF1|pad=<pad_len>|freq=<symbol:weight,...>|

    Args:
        pad_len: Number of padding bits at the end (0-7).
        freq: Dict mapping symbol (0-255) to weight (>=1).

    Returns:
        Header string ending with a trailing '|'.
    
    Raises:
        ValueError: If the pad, or freq values fail validation.
    """

    if not (0 <= pad_len <= 7):
        raise ValueError(f"pad length out of range: {pad_len}")
    
    for symbol, weight in freq.items():
        if not isinstance(symbol, int):
            raise ValueError("symbol must be integer.")
        if not isinstance(weight, int):
            raise ValueError("weight must be integer.")
        if not (0 <= symbol <= 255):
            raise ValueError("symbol must be 0-255")
        if weight < 1:
            raise ValueError("weight must be >= 1. ")

    pad = f"pad={pad_len}"
    
    freq_keys= sorted(freq.keys())
    freq_string = [f"{key}:{freq[key]}" for key in freq_keys]
    freq_string = "freq=" + ",".join(freq_string)

    header_list = [FULL_VERSION, pad, freq_string]
    header = "|".join(header_list) + "|"

    return header

def decode_header_and_payload(data: bytes) -> tuple[HeaderInfo, bytes]:
    """
    Parse the header from a compressed byte stream and return
    (header_info, body_bytes).
    """
    header_end = None
    n_divider = 0
    for idx, byte in enumerate(data):
        if byte == ord("|"):
            n_divider +=1
            if n_divider == 3:
                header_end = idx + 1
                break

    if n_divider < 3:
        raise ValueError("Incomplete or malformed header: expected 3 '|' separators")

    if header_end is None:
        raise ValueError("Incomplete header: did not find 3 separators")

    header_bytes = data[:header_end]
    header_str = header_bytes.decode("utf-8")
    body_bytes = data[header_end:]

    header_info = decode_header(header_str)

    return header_info, body_bytes



def decode_header(header: str)-> HeaderInfo:
    """
    Decode the header from a Huffman-compressed string.

    The expected header format is:
        HUF<version>|pad=<pad_len>|freq=<symbol:weight,...>|

    Examples:
        HUF1|pad=3|freq=97:4,98:5,99:1|

    Args:
        header: string containing the version, padding and frequency set.

    Returns:
        HeaderInfo: A NamedTuple containing
            - version: full version string (e.g. "HUF1")
            - pad_len: number of padding bits (0-7)
            - freq: dict mapping symbols (0-255) to weights (>=1)

    Raises:
        ValueError: If the header is malformed or version, pad, or freq
            values fail validation.
    """

    header_fields = header.split("|")
    if len(header_fields) < 3:
        raise ValueError("Unknown header format")
    
    version = header_fields[0]
    pad_field = header_fields[1]
    freq_string_field = header_fields[2]

    version = _parse_version(version)
    pad_len = _parse_pad(pad_field)
    freq = _parse_freq(freq_string_field)

    return HeaderInfo(version, pad_len, freq)
    

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
    if not (0 <= pad_len <= 7):
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
    
    
    
 