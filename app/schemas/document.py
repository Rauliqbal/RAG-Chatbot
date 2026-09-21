from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
  filename: str
  pages: int
  characters: int
  message: str