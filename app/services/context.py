
def build_context(results) -> str:
    documents = results.get(
        "documents",
        [[]]
    )[0]

    context = "\n\n".join(
        documents
    )
    
    return context