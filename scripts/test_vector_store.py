from app.services.embedding import generate_embeddings
from app.services.vector_store import add_documents


documents = [
    "Database normalization reduces data redundancy.",
    "First Normal Form requires atomic values.",
    "Second Normal Form removes partial dependencies.",
]


embeddings = generate_embeddings(documents)


ids = [
    "chunk-1",
    "chunk-2",
    "chunk-3",
]


metadatas = [
    {
        "source": "database.pdf",
        "page": 1,
    },
    {
        "source": "database.pdf",
        "page": 2,
    },
    {
        "source": "database.pdf",
        "page": 3,
    },
]


add_documents(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
)


print("Documents inserted successfully.")