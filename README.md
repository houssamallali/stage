# stage

A tiny utility to extract text from PDF files. It first attempts to read embedded
text and falls back to OCR for scanned pages.

## Setup

1. Install the Python dependencies:
   ```bash
   pip install pymupdf pytesseract pillow
   ```
2. Install the Tesseract OCR engine (example for Debian/Ubuntu):
   ```bash
   sudo apt-get install tesseract-ocr
   ```

## Usage

```bash
python pdf_reader.py path/to/document.pdf
```

The extracted text is printed to standard output.
