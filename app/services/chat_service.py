from ollama import chat,ResponseError
from app.config import OLLAMA_MODEL


SYSTEM_PROMPT = """
Kamu adalah AI assistant untuk membantu developer pemula.

Aturan:
- Gunakan bahasa Indonesia.
- Jelaskan dengan sederhana.
- Berikan contoh jika diperlukan.
- Jangan menggunakan istilah teknis tanpa menjelaskannya. 

berikan contohnya jika diperlukan
"""

def generate_response(message: str ) ->str :
  try:
    response = chat(
        model=OLLAMA_MODEL,
        messages=[
          {
            "role": "user",
            "content": SYSTEM_PROMPT
          },
          {
            "role": "user",
            "content": message
          }
        ],
      )
      
    return response.message.content
    
  except ResponseError as error:
    if error.status_code == 404:
      raise RuntimeError(
        f"Model '{OLLAMA_MODEL}' tidak ditemukana"
      )
    
    raise RuntimeError(
      f"Ollama error: {error.error}"
    )