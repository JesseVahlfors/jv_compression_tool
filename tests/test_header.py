import pytest
from compression_tool.header import build_header, decode_header, HeaderInfo, FULL_VERSION


def test_header_io():
    pad_len = 3
    freq = {97: 4, 98: 5, 99: 1}
    codestring = "101001101"

    header = build_header(pad_len, freq)
    parsed = decode_header(header + codestring)

    assert parsed.version == FULL_VERSION
    assert parsed.pad_len == 3
    assert parsed.freq == {97: 4, 98: 5, 99: 1}
    assert parsed.payload == codestring

def test_build_header_string():
    pad_len = 3
    freq = {98: 5, 97: 4,  99: 1}

    header = build_header(pad_len, freq)

    assert header == "HUF1|pad=3|freq=97:4,98:5,99:1|"

def test_decode_header_version_string():
    pad_len = 3
    freq = {97: 4, 98: 5, 99: 1}
    codestring = "101001101"

    header = build_header(pad_len, freq)
    parsed = decode_header(header + codestring)

    assert parsed.version == FULL_VERSION
    assert parsed.payload == codestring

@pytest.mark.parametrize("invalid_version", [
    "ZIP1",
    "HUF",
    "HUF-1",
    "HUFFZAH"
])

def test_decode_header_wrong_version_check(invalid_version):
    codestring = "101001101"
    header = f"{invalid_version}|pad=3|freq=97:4,98:5,99:1|"
    
    with pytest.raises(ValueError):
        decode_header(header + codestring)

@pytest.mark.parametrize("invalid_pad", [
    "pad=ab",
    "pad=9",
    "pad=-1",
    "pad=9823"
])

def test_decode_header_reject_bad_pad_range(invalid_pad):
    codestring = "101001101"
    header = f"HUF1|{invalid_pad}|freq=97:4,98:5,99:1|"
    
    with pytest.raises(ValueError):
        decode_header(header + codestring)


@pytest.mark.parametrize("malformed_pad", [
    "pad=",
    "pad= ",
    "pad=abc",
    "pad3",
    "pad-1",
])

def test_decode_header_malformed_pad_field(malformed_pad):
    codestring = "101001101"
    header = f"HUF1|{malformed_pad}|freq=97:4,98:5,99:1|"
    
    with pytest.raises(ValueError):
        decode_header(header + codestring)

@pytest.mark.parametrize("malformed_freq", [
    "freq= ",
    "freq=abc",
    "freq3",
    "freq-1",
])

def test_decode_header_malformed_freq_field(malformed_freq):
    codestring = "101001101"
    header = f"HUF1|pad=3|{malformed_freq}|"
    
    with pytest.raises(ValueError):
        decode_header(header + codestring)

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
    codestring = "101001101"
    header = f"HUF1|pad=3|{invalid_freq}|"
    with pytest.raises(ValueError):
        decode_header(header + codestring)

def test_decode_header_valid_with_empty_freq():
    codestring = "101001101"
    header = "HUF1|pad=3|freq=|"
    print(header)

    parsed = decode_header(header + codestring)
    assert parsed.freq == {}