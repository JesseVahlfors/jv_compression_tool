from compression_tool import frequency

def test_frequency_count():
    data = b"aaabbc"
    freq = frequency.count_frequencies(data)
    assert freq == {97: 3, 98: 2, 99: 1}  # ASCII values for 'a', 'b', 'c'
