from app.services.chunker import chunk_text
from app.services.document_service import extract_text_from_pdf
from app.services.embedding import generate_embeddings
from app.services.vector_store import add_documents


def ingest_document(
    file_path: str,
    filename: str,
):
    text, pages = extract_text_from_pdf(
        file_path
    )

    chunks = chunk_text(text)

    embeddings = generate_embeddings(
        chunks
    )

    ids = [
        f"{filename}-chunk-{index}"
        for index in range(len(chunks))
    ]

    metadatas = [
        {
            "source": filename,
            "chunk_index": index,
        }
        for index in range(len(chunks))
    ]

    add_documents(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    return {
        "filename": filename,
        "pages": pages,
        "chunks": len(chunks),
    }