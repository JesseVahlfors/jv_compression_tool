from compression_tool.frequency import count_frequencies

def test_frequency_count():
    data = b"aaabbc"
    freq = count_frequencies(data)
    assert freq == {97: 3, 98: 2, 99: 1}  # ASCII values for 'a', 'b', 'c'
