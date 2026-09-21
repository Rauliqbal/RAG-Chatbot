from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import generate_response
from app.services.rag import generate_rag_response

router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"]
)


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    answer = generate_rag_response(
        request.message
    )

    return ChatResponse(
        answer=answer
    )