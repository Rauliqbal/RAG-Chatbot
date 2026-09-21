# Junet RAG

A local Retrieval-Augmented Generation (RAG) application built with Python and FastAPI.

Junet is designed as a learning project for understanding how a RAG system works from document ingestion to AI-generated answers.

## ✨ Features

* 📄 PDF document ingestion
* ✂️ Text extraction and chunking
* 🔎 Semantic search with embeddings
* 🧠 Local LLM inference
* 💬 Question answering based on document context
* 🚀 REST API with FastAPI
* 💾 Local vector database
* 🔒 Designed to run locally without sending documents to a third-party LLM API

## 🏗️ Architecture

```text
                    JUNET RAG
                       │
             ┌─────────┴─────────┐
             │                   │
        DOCUMENT INGESTION      CHAT
             │                   │
            PDF              User Question
             ↓                   ↓
        Text Extraction       Embedding
             ↓                   ↓
          Chunking               │
             ↓                   ↓
        BGE-M3 Embedding         │
             ↓                   ↓
          ChromaDB ←──── Similarity Search
             │                   │
             │            Relevant Chunks
             │                   ↓
             │             Context Builder
             │                   ↓
             └────────────→ Gemma 3
                                 ↓
                              Answer
```

## 🧰 Tech Stack

### Backend

* Python 3.11+
* FastAPI
* Uvicorn
* Pydantic

### AI / RAG

* **Gemma 3** — local Large Language Model
* **BAAI/bge-m3** — multilingual embedding model
* **ChromaDB** — vector database

### Document Processing

* PyMuPDF

## 📁 Project Structure

```text
junet/
├── app/
│   ├── api/
│   │   └── chat_api.py
│   ├── core/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── data/
│   └── documents/
│
├── tests/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/
```

The project structure may evolve as new RAG features are implemented.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd junet
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🤖 Setup Gemma 3

Junet uses Ollama to run Gemma locally.

Install Ollama, then pull the model:

```bash
ollama pull gemma3:4b
```

Test the model:

```bash
ollama run gemma3:4b
```

Make sure the Ollama service is running before starting the API.

## 🧠 Embedding Model

Junet uses:

```text
BAAI/bge-m3
```

BGE-M3 is used to convert document chunks and user questions into vector representations.

The vectors are then stored in ChromaDB for semantic retrieval.

## ▶️ Run the API

Start the FastAPI development server:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔌 API

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Chat

```http
POST /api/v1/chat
```

Request:

```json
{
  "question": "Apa itu database?"
}
```

Response:

```json
{
  "answer": "Database adalah ..."
}
```

The final implementation may change as the RAG pipeline develops.

## 🔄 RAG Pipeline

Junet follows these main stages.

### 1. Document Ingestion

A PDF is uploaded to the application.

```text
PDF
 ↓
PyMuPDF
 ↓
Plain Text
```

### 2. Chunking

The extracted text is divided into smaller pieces.

```text
Document
 ↓
Chunks
 ↓
Chunk 1
Chunk 2
Chunk 3
...
```

### 3. Embedding

Each chunk is converted into a vector using BGE-M3.

```text
Text Chunk
 ↓
BGE-M3
 ↓
Vector
```

### 4. Vector Storage

Vectors are stored in ChromaDB.

```text
Chunk + Embedding
        ↓
    ChromaDB
```

### 5. Retrieval

When the user asks a question, the question is embedded and compared against stored vectors.

```text
Question
   ↓
BGE-M3
   ↓
Query Vector
   ↓
Similarity Search
   ↓
Relevant Chunks
```

### 6. Generation

The retrieved chunks are provided to Gemma 3 as context.

```text
Question
+
Retrieved Context
        ↓
     Gemma 3
        ↓
      Answer
```

## 🎯 Project Goals

This project is intended to demonstrate the fundamentals of building a RAG system without hiding the core concepts behind a high-level framework.

The main learning goals are:

* Understanding embeddings
* Understanding vector databases
* Understanding semantic search
* Understanding document chunking
* Understanding retrieval
* Understanding prompt construction
* Understanding how an LLM works with retrieved context
* Building AI APIs with FastAPI
* Running open-source AI models locally

## 🛣️ Roadmap

- ✅ Step 1  FastAPI
- ✅ Step 2  API structure
- ✅ Step 3  Request/Response schema
- ✅ Step 4  Service layer
- ✅ Step 5  Local LLM
- ✅ Step 6  PDF upload API
- ✅ Step 7  PDF text extraction
- ✅ Step 8  Chunking
- ⬜ Step 9  Embedding
- ⬜ Step 10 Vector database
- ⬜ Step 11 Retrieval
- ⬜ Step 12 RAG
- ⬜ Step 13 Streaming response
- ⬜ Step 14 Authentication
- ⬜ Step 15 Docker

* [x] FastAPI project setup
* [ ] Connect Gemma 3
* [ ] PDF upload
* [ ] PDF text extraction
* [ ] Text chunking
* [ ] BGE-M3 embeddings
* [ ] ChromaDB integration
* [ ] Semantic retrieval
* [ ] RAG prompt construction
* [ ] Context-aware answers
* [ ] Source/document references
* [ ] Conversation history
* [ ] Streaming responses
* [ ] RAG evaluation
* [ ] Frontend chat interface

## 🔐 Privacy

Junet is designed around local AI processing.
Documents can remain on the local machine, while the LLM runs locally through Ollama.
Do not commit private documents, API keys, credentials, or environment files to the repository.

## 📌 Status

> 🚧 Junet is currently under active development.

The architecture and API may change as new RAG components are introduced.

## 📄 License

This project is intended for learning and experimentation.
