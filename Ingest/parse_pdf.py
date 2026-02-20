# Với PDF có text layer

#pip install pypdf
#pip install pdfplumber

import pdfplumber

with pdfplumber.open("./Ingest/Data/VA Parking Lease Agreement.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"
    print(text)
    
# Với PDF scan (image)
# pip install pytesseract
# Tiếng Việt: tesseract-ocr-vie