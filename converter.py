import sys
from pdf2image import convert_from_path

def pdf_to_png(pdf_path):
    images = convert_from_path(pdf_path, dpi=300)
    output_prefix = pdf_path.rsplit(".", 1)[0]  # Remove extension

    for i, img in enumerate(images):
        img.save(f"{output_prefix}_page_{i+1}.png", "PNG")
    print(f"Extracted {len(images)} pages as PNGs.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <pdf_file>")
        sys.exit(1)

    pdf_to_png(sys.argv[1])

