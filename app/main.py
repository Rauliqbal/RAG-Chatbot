from fastapi import FastAPI
from app.api.chat_api import router as chat_router
from app.api.document_api import router as document_router

app = FastAPI(
  title= 'JunetAI',
  version= '0.0.1'
)

app.include_router(chat_router)
app.include_router(document_router)

@app.get("/")
def root():
  return {
    "message" : "JunetAI is online"
  }
  
  
@app.get('/health')
def health():
  return {
    "status" : "im fine"
  }