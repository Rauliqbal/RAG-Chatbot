from app.services.rag import generate_rag_response

question = "Apa itu python?"

answer = generate_rag_response(
    question
)

print("\nAI:")
print(answer)