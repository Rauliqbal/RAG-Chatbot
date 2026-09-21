from app.services.chunker import chunk_text


text = """
Database normalization is a technique
used to organize data in relational databases.

The first normal form requires atomic values.

The second normal form removes partial dependency.

The third normal form removes transitive dependency.
"""


chunks = chunk_text(
    text,
    chunk_size=100,
    overlap=20,
)


for index, chunk in enumerate(chunks):
    print(f"\n--- Chunk {index + 1} ---")
    print(chunk)