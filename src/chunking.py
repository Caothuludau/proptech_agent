
"""
RecursiveCharacterTextSplitter:
    Thử split theo paragraph trước
    Nếu quá dài → split theo sentence
    Nếu vẫn dài → split theo character
    Nó ưu tiên semantic boundary trước khi cắt bừa.
    Đó là lý do nó tốt hơn split thuần ký tự.
"""

def chunk_document(text: str, chunk_size=1000, chunk_overlap=200):
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_text(text)

    return chunks

    # print(f"--- THỬ NGHIỆM: Size {chunk_size}, Overlap {chunk_overlap} ---")
    # print(f"Tổng số chunk tạo ra: {len(chunks)}")
    # In thử để kiểm tra
    # for i, chunk in enumerate(chunks[:2]):
    #     print(f"\nChunk {i+1} (Độ dài {len(chunk)}):")
    #     print(f"'{chunk[:100]}...' [NỘI DUNG LƯỢC BỚT] ...'{chunk[-100:]}'")
    # for i, chunk in enumerate(chunks[:10]):
    #     print(f"\n--- Chunk {i} ---\n")
    #     print(chunk)
    print("-" * 50)

# txt_path="./Output/VA Parking Lease Agreement.txt"

# Chạy test 3 loại theo yêu cầu của bạn
# with open(txt_path, "r", encoding="utf-8") as f:
#     text = ""
#     text = f.read()

# 1. Level 1: Fixed size
# test_chunking(text, 1000, 100)

# 2. 1000 characters
# test_chunking(text, 1000, 0)

# 3. Overlap 100 (với size 500 để bạn dễ so sánh)
# test_chunking(text, 500, 100)