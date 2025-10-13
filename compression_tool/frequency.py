
def count_frequencies(data):
    """Counts the frequency of each byte in the given data."""
    freq = {}
    for byte in data:
        if byte in freq:
            freq[byte] += 1
        else:
            freq[byte] = 1
    return freq

