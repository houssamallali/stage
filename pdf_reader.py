import io
from typing import List

import fitz  # PyMuPDF
import pytesseract
from PIL import Image


def extract_pdf_text(pdf_path: str) -> str:
    """Extract text from a PDF, using OCR for image-only pages.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        The extracted text as a single string.
    """
    text_parts: List[str] = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text().strip()
            if text:
                text_parts.append(text)
            else:
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                ocr_text = pytesseract.image_to_string(img).strip()
                text_parts.append(ocr_text)
    return "\n".join(filter(None, text_parts))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract text from PDFs with OCR fallback.")
    parser.add_argument("pdf", help="Path to the PDF file")
    args = parser.parse_args()

    print(extract_pdf_text(args.pdf))
