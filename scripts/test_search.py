
from app.services.embedding import generate_embedding
from app.services.vector_store import search_documents

question = "Jelaskan apa itu normalisasi database"

query_embedding = generate_embedding(question)

results = search_documents(
    query_embedding=query_embedding,
    limit=3
)

print(results)