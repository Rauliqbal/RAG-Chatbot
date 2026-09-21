from app.services.retrieval import retrieve_documents

question="Apa itu python?"

results = retrieve_documents(
    question,
    limit=3
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]

for index, (document, metadata) in enumerate(
    zip(documents,metadatas),
    start=1,
):
    print(f"\n --- Result {index} ---")
    print(document)
    print("Metadata:", metadata)