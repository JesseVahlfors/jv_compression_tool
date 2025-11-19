from collections import Counter

def build_frequency_table(data):
    """
Build a frequency table for Huffman compression.

Args:
    text: The original input string to compress.

Returns:
    A dict mapping byte/symbol integers (0-255) to frequency counts (>= 1).
"""
    return Counter(data)

