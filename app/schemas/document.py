from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
  filename: str
  pages: int
  characters: int
  preview:str
  message: str