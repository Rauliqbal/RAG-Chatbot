from fastapi import APIRouter,File,HTTPException,UploadFile
from pathlib import Path
from uuid import uuid4

from app.schemas.document import DocumentUploadResponse
from app.services.document_service import extract_text_from_pdf

router = APIRouter( 
  prefix="/api/v1/document",
  tags=["Document"]
)


DOCUMENT_DIR = Path("data/documents")
DOCUMENT_DIR.mkdir(
  parents=True,
  exist_ok=True
)

@router.post("/upload",
             response_model=DocumentUploadResponse)
async def upload_document (
  file: UploadFile = File(...)
):
  if file.content_type != 'application/pdf':
    raise HTTPException(
      status_code=400,
      detail="Please upload file PDF"
    )
  
  document_id = str(uuid4())
  filename = file.filename
  
  file_path = (
        DOCUMENT_DIR
        / f"{document_id}.pdf"
    )

  content = await file.read()

  file_path.write_bytes(content)

  text, pages = extract_text_from_pdf(
        str(file_path)
    )

  return DocumentUploadResponse(
        filename=filename,
        pages=pages,
        characters=len(text),
        message="Document uploaded successfully",
    )