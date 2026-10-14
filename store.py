
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

def search(question, n_results=3):
    collection = get_collection()
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )
    hits = []
    #return data in similar format to chunks
    for text, meta in zip(results['documents'][0], results['metadatas'][0]):
        hits.append({
            "text": text,
            "page_number": meta["page_number"]
        })
    return hits