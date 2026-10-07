from pypdf import PdfReader
reader = PdfReader("lease.pdf")
#print(len(reader.pages), " pages found")

for number, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"Page {number + 1}:\n{text}\n")