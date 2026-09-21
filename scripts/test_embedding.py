from app.services.embedding import generate_embedding


text = """
Database normalization is a technique
used to organize data in relational databases.
"""


embedding = generate_embedding(text)


print("Embedding length:", len(embedding))
print("First 10 values:", embedding[:10])