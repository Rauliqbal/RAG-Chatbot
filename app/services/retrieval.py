from app.services.embedding import generate_embedding
from app.services.vector_store import search_documents

def retrieve_documents(
    question: str,
    limit: int = 3
) :
    query_embedding = generate_embedding(
        question
    )
    
    results = search_documents(
        query_embedding=query_embedding,
        limit=limit
    )
    
    return results