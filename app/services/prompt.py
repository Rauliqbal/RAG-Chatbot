def build_rag_prompt(
    question: str,
    context: str
) -> str:
    return f"""
Kamu adalah AI assistant yang menjawab
pertanyaan berdasarkan dokumen yang diberikan.

Gunakan hanya informasi yang terdapat
di dalam CONTEXT.

Jika jawaban tidak ditemukan di dalam
CONTEXT, katakan bahwa informasi tersebut
tidak ditemukan dalam dokumen.

Jangan mengarang informasi.

CONTEXT:
--------------------
{context}
--------------------

QUESTION:
{question}

Jawab dalam bahasa Indonesia yang jelas
dan mudah dipahami.
"""