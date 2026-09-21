from app.services.retrieval import retrieve_documents
from app.services.context import build_context


question = "Apa itu python?"


results = retrieve_documents(
    question,
    limit=3,
)


context = build_context(results)


print(context)