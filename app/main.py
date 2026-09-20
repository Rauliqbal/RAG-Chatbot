from fastapi import FastAPI
from app.api.chat_api import router as chat_router

app = FastAPI(
  title= 'JunetAI',
  version= '0.0.1'
)

app.include_router(chat_router)

@app.get("/")
def root():
  return {
    "message" : "JunetAI is online"
  }
  