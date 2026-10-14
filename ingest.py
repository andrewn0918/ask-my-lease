from pypdf import PdfReader
from store import get_collection, store_chunks

reader = PdfReader("lease.pdf")

def chunk_text(text, chunk_size=400):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(' '.join(words[i:i + chunk_size]))
    return chunks

chunks = []
for number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    for piece in chunk_text(text):
        chunks.append({
            "text": piece,
            "page_number": number
        })


count = store_chunks(chunks)
print(count, "chunks stored")