# Với PDF có text layer

#pip install pypdf
#pip install pdfplumber

pdf_path="./data/VA Parking Lease Agreement.pdf"
txt_path=".Output/VA Parking Lease Agreement.txt"

import pdfplumber

with pdfplumber.open(pdf_path) as pdf:
    text = ""
    # Kiểm tra nếu page có nội dung để tránh lỗi NoneType
    for page in pdf.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extraction completed! File saved at: {txt_path}")

# Với PDF scan (image)
# pip install pytesseract
# Tiếng Việt: tesseract-ocr-vie
