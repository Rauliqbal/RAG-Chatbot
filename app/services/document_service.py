import fitz

def extract_text_from_pdf(file_path: str) -> tuple[str,int]:
  document = fitz.open(file_path)
  
  text = ""

  for page in document:
    text += page.get_text()
    text += "\n"
    
  pages = len(document)

  document.close()
  
  return text,pages