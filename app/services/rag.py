from ollama import chat

from app.config import OLLAMA_MODEL
from app.services.context import build_context
from app.services.prompt import build_rag_prompt
from app.services.retrieval import retrieve_documents

def generate_rag_response(
    question:str
):
    
    results = retrieve_documents(
        question,
        limit=3,
    )
    
    context = build_context(
        results
    )
    
    prompt = build_rag_prompt(
        question=question,
        context=context
    )
    
    response = chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    return response.message.content