import chromadb

client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_or_create_collection(
    name="documents"
)

def add_documents(
  ids: list[str],
  documents: list[str],
  embeddings: list[list[float]],
  metadatas: list[dict],
) : 
  collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
  )
  
def search_documents(
    query_embedding: list[float],
    limit: int = 3
):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
    return results