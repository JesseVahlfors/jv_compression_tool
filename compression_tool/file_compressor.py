from pathlib import Path
from compression_tool.compressor import compress
import sys

def compress_file(path: str) -> bytes:
    with open(path, "rb") as file:
        data = file.read() #Using "rb" mode to read the file as bytes

    compressed_data = compress(data)

    with open(path + ".huff", "wb") as out:
        out.write(compressed_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_compressor.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    compress_file(file_path)
    print(f"File compressed and saved as {file_path}.huff")