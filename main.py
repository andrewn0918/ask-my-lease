from pypdf import PdfReader
reader = PdfReader("lease.pdf")
print(len(reader.pages), " pages found")