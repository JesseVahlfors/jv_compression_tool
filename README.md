# Compression Tool (Huffman Coding in Pure Python)

A lightweight, fully tested Huffman compression library with both byte-level and file-level APIs.

This project implements a complete Huffman compression pipeline from scratch, including:

- Frequency counting
- Min-heap construction
- Huffman tree generation
- Code map building
- Bit packing/unpacking
- Header encoding/decoding
- High-level compression & decompression functions
- File-based compressor and decompressor
- Full test suite (unit + integration)

The goal is to provide a clear, modular reference implementation that is easy to study, extend, and reuse — including on a future demo page.

---

## ✨ Features

- 🔧 **Pure Python implementation**
- 🧪 **Fully tested with pytest**
- 📄 **File compression support**
- 🔁 **Round-trip safe**
- 📦 **Simple API**:
  - `compress_bytes(data: bytes)`
  - `decompress_bytes(data: bytes)`
  - `compress_file(path)`
  - `decompress_file(path)`
- 🧩 **Modular internal architecture**
- 🔌 **Ready for packaging to PyPI**

---

## 🚀 Installation (Development)

Clone the repo and install in editable mode:

```bash
git clone https://github.com/JesseVahlfors/jv_compression_tool.git
cd jv_compression_tool
pip install -e .
```

Then you can import it anywhere:

```python
import compression_tool
```

---

## 🧩 Usage

1. Compressing bytes

   ```python
   from compression_tool import compress_bytes, decompress_bytes

   data = b"hello world"
   compressed = compress_bytes(data)
   original = decompress_bytes(compressed)

   assert original == data
   ```

2. Compressing files

   ```python
   from compression_tool import compress_file, decompress_file

   result = compress_file("example.txt")

   print("Original size:", result.original_size)
   print("Compressed size:", result.compressed_size)

   decomp = decompress_file(result.output_path)
   ```

The file APIs return small dataclasses:

- CompressionResult
- DecompressionResult

---

## 🧱 Project Structure

Current recommended packaging structure:

```
jv_compression_tool/
├── pyproject.toml
├── README.md
├── src/
│   └── compression_tool/
│       ├── __init__.py
│       ├── compressor.py
│       ├── decompressor.py
│       ├── file_compressor.py
│       ├── file_decompressor.py
│       ├── frequency.py
│       ├── tree.py
│       ├── build_tree.py
│       ├── code_map.py
│       ├── lookup.py
│       ├── header.py
│       └── utils/
│           ├── heapify.py
│           └── bitutils.py
└── tests/
    ├── test_file_io.py
    ├── test_compressor.py
    ├── test_decompressor.py
    └── data/
        └── test.txt
```

---

## Header Format

This project currently uses a simple text-based header:

```
HUF1|pad=<pad_len>|freq=symbol:weight,...|
```

- `HUF1` = Magic string + version tag for this header format.
- `pad` = Number of padding bits at the end of the compressed data.
- `freq` = Frequency table, where each symbol is represented as `<symbol>:<weight>`.
- Each symbol is stored as its integer byte value (e.g. `104` = ASCII `"h"`).
- Ends with `|` for easy parsing.

### Example:

```
HUF1|pad=3|freq=104:1,101:1,108:3,111:2|
```

A binary header format may be introduced later.

---

## Development

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest
```


## 🧪 Testing

Run all tests:

```bash
pytest
```

Run fast tests only:

```bash
pytest -m "not slow"
```

Slow tests (e.g., large Les Mis file) are marked:

```python
@pytest.mark.slow
@pytest.mark.skipif(not RUN_SLOW_TESTS, reason="Slow test disabled")
```

---

## 📈 Performance

Huffman compression becomes effective when:

- Input is large
- Symbol distribution is skewed
- Repetition exists

Small files may grow slightly due to header overhead — this is normal.

---

## 🗺 Future Improvements

- CLI tool (huff compress file.txt)
- Binary header format
- Streaming compression
- Publish to PyPI

---

## 📜 License

MIT License.
