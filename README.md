# Compression Tool (Huffman Coding in Pure Python)

A lightweight, fully tested Huffman compression library with both byte-level and file-level APIs.

This project implements a complete Huffman compression pipeline from scratch, including:

- Frequency counting  
- Min-heap construction  
- Huffman tree generation  
- Code map building  
- Bit packing/unpacking  
- Header encoding/decoding  
- High-level compression & decompression  
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
  - `compress_bytes(data: bytes) -> bytes`
  - `decompress_bytes(data: bytes) -> bytes`
  - `compress_file(path) -> CompressionResult`
  - `decompress_file(path) -> DecompressionResult`
- 🧩 **Modular internal structure**  
- 📦 **Published as a PyPI package**

---

## 📦 Installation

Install from PyPI:

```bash
pip install jv-compression-tool
```

Then:

```python
import compression_tool
```

---

## 🧩 Usage

### 1. Compressing bytes

```python
from compression_tool import compress_bytes, decompress_bytes

data = b"hello world"
compressed = compress_bytes(data)
restored = decompress_bytes(compressed)

assert restored == data
```

### 2. Compressing files

```python
from compression_tool import compress_file, decompress_file

result = compress_file("example.txt")

print("Original size:", result.original_size)
print("Compressed size:", result.compressed_size)

decomp = decompress_file(result.output_path)
assert decomp.output_path.read_bytes() == Path("example.txt").read_bytes()
```

The file APIs return simple dataclasses:

- `CompressionResult`
- `DecompressionResult`

---

## 🧱 Project Structure

The project uses a `src/` layout for clean packaging:

```
jv_compression_tool/
├── pyproject.toml
├── README.md
├── LICENSE
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
    ├── test_header.py
    ├── test_heapify.py
    ├── test_build_tree.py
    ├── test_compressor.py
    ├── test_decompressor.py
    ├── test_file_io.py
    └── data/
        └── test.txt
```

(Test file names are illustrative — your exact structure may differ.)

---

## 🔍 Header Format

This project currently uses a simple text-based header:

```
HUF1|pad=<pad_len>|freq=symbol:weight,...|
```

- `HUF1` – Magic string + version tag  
- `pad` – Number of padding bits added to the final byte  
- `freq` – A comma-separated table of `<symbol>:<weight>`  
- Symbols use their integer byte value (e.g. `104` = `b"h"`)

### Example

```
HUF1|pad=3|freq=104:1,101:1,108:3,111:2|
```

A more compact binary header format may be introduced later.

---

## 🛠 Development

To set up a local development environment:

```bash
git clone https://github.com/JesseVahlfors/jv_compression_tool.git
cd jv_compression_tool

python -m venv .venv
.\.venv\Scripts\activate          # or: source .venv/Scripts/activate

pip install -r requirements.txt
pip install -e .
```

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

Run fast tests only (skipping slow ones):

```bash
pytest -m "not slow"
```

Slow tests (e.g., using a large “Les Misérables” file) are marked:

```python
@pytest.mark.slow
@pytest.mark.skipif(not RUN_SLOW_TESTS, reason="Slow test disabled")
```

---

## 📈 Performance Notes

Huffman compression works best when:

- Input is large  
- Symbol distribution is uneven  
- Repetition exists in the data  

Small files may grow slightly due to header overhead — this is expected.

---

## 🗺 Future Improvements

- CLI tool (e.g., `huff compress file.txt`)
- Binary header format
- Streaming compression
- Web/demo integration

---

## 📜 License

Licensed under the [MIT License](LICENSE).
