import pytest
from compression_tool.header import (
    build_header,
    decode_header,
    HeaderInfo,
    FULL_VERSION,
    decode_header_and_payload,
)
from compression_tool.utils.bitutils import pack_bits, unpack_bits

def test_header_io():
    freq = {97: 4, 98: 5, 99: 1}
    codestring = "101001101"

    body_bytes, pad_len = pack_bits(codestring)

    header_str = build_header(pad_len, freq)
    header_bytes = header_str.encode("utf-8")

    data = header_bytes + body_bytes

    header_info, parsed_body = decode_header_and_payload(data)

    assert header_info.version == FULL_VERSION
    assert header_info.pad_len == pad_len
    assert header_info.freq == freq

    assert parsed_body == body_bytes

    restored_codestring = unpack_bits(parsed_body, pad_len)
    assert restored_codestring == codestring

def test_build_header_string():
    pad_len = 3
    freq = {98: 5, 97: 4,  99: 1}

    header = build_header(pad_len, freq)

    assert header == "HUF1|pad=3|freq=97:4,98:5,99:1|"

def test_decode_header_and_payload_io():
    pad_len = 5
    freq = {65: 2, 66: 1}
    fake_body = b"\x80\x55"

    header_str = build_header(pad_len, freq)
    header_bytes = header_str.encode("utf-8")
    header_info, body_bytes = decode_header_and_payload(header_bytes + fake_body)

    assert header_info.version == "HUF1"
    assert header_info.pad_len == 5
    assert header_info.freq == {65:2, 66:1}
    assert body_bytes == fake_body

def test_decode_header_and_payload_empty_input():
    header_str = build_header(0, {})
    header_bytes = header_str.encode("utf-8")
    data = header_bytes

    header_info, body_bytes = decode_header_and_payload(data)

    assert header_info.version == "HUF1"
    assert header_info.pad_len == 0
    assert header_info.freq == {}
    assert body_bytes == b""  # empty body


def test_decode_header_version_string():
    pad_len = 3
    freq = {97: 4, 98: 5, 99: 1}

    header = build_header(pad_len, freq)
    parsed = decode_header(header)

    assert parsed.version == FULL_VERSION

@pytest.mark.parametrize("invalid_version", [
    "ZIP1",
    "HUF",
    "HUF-1",
    "HUFFZAH"
])

def test_decode_header_wrong_version_check(invalid_version):
    header = f"{invalid_version}|pad=3|freq=97:4,98:5,99:1|"
    
    with pytest.raises(ValueError):
        decode_header(header)

@pytest.mark.parametrize("invalid_pad", [
    "pad=ab",
    "pad=9",
    "pad=-1",
    "pad=9823"
])

def test_decode_header_reject_bad_pad_range(invalid_pad):
    header = f"HUF1|{invalid_pad}|freq=97:4,98:5,99:1|"
    
    with pytest.raises(ValueError):
        decode_header(header)


@pytest.mark.parametrize("malformed_pad", [
    "pad=",
    "pad= ",
    "pad=abc",
    "pad3",
    "pad-1",
])

def test_decode_header_malformed_pad_field(malformed_pad):
    header = f"HUF1|{malformed_pad}|freq=97:4,98:5,99:1|"
    
    with pytest.raises(ValueError):
        decode_header(header)

@pytest.mark.parametrize("malformed_freq", [
    "freq= ",
    "freq=abc",
    "freq3",
    "freq-1",
])

def test_decode_header_malformed_freq_field(malformed_freq):
    header = f"HUF1|pad=3|{malformed_freq}|"
    
    with pytest.raises(ValueError):
        decode_header(header)

@pytest.mark.parametrize("invalid_freq", [
    "freq=98",
    "freq=98:",
    "freq=:7",
    "freq=-9:7",
    "freq=98:-7",
    "freq=98:7,",
    "freq=,98:7",
    "freq=256:7",
    "freq=97:0",
    "freq=98:7:89",
    "freq=98:7,98:3"
])

def test_decode_header_reject_bad_freq_range(invalid_freq):
    header = f"HUF1|pad=3|{invalid_freq}|"
    with pytest.raises(ValueError):
        decode_header(header)

def test_decode_header_valid_with_empty_freq():
    header = "HUF1|pad=3|freq=|"

    parsed = decode_header(header)
    assert parsed.freq == {}