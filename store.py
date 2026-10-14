
import chromadb

def get_collection():
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_or_create_collection(name="lease")

def store_chunks(chunks):
    collection = get_collection()
    collection.upsert(
        ids = [f"chunk_{i}" for i in range(len(chunks))],
        metadatas = [{"page_number": chunk["page_number"]} for chunk in chunks],
        documents = [chunk["text"] for chunk in chunks]
    )
    return collection.count()