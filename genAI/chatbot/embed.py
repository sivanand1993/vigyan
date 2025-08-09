import os
from typing import List, Dict, Any
from pypdf import PdfReader
from docx import Document
import tiktoken
import numpy as np
from openai import OpenAI



# --- File Loaders ---
def load_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def load_docx(path: str) -> str:
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def load_any(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return load_pdf(path)
    elif ext == ".docx":
        return load_docx(path)
    else:
        return load_txt(path)

# --- Chunking ---
def chunk_text(text: str, chunk_tokens: int = 400, overlap: int = 60, model: str = "gpt-4o-mini") -> List[str]:
    enc = tiktoken.encoding_for_model(model) if model else tiktoken.get_encoding("cl100k_base")
    toks = enc.encode(text)
    chunks = []
    i = 0
    while i < len(toks):
        chunk = toks[i:i+chunk_tokens]
        chunks.append(enc.decode(chunk))
        i += (chunk_tokens - overlap)
    return [c.strip() for c in chunks if c.strip()]

# --- Embedding ---
def embed_texts(texts: List[str], model: str = "text-embedding-3-small") -> np.ndarray:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    resp = client.embeddings.create(model=model, input=texts)
    vecs = [d.embedding for d in resp.data]
    X = np.array(vecs, dtype="float32")
    norms = np.linalg.norm(X, axis=1, keepdims=True) + 1e-10
    return X / norms  # cosine normalization

# --- Prepare documents ---
def prepare_docs(paths: List[str], source_label: str = None) -> Dict[str, Any]:
    all_chunks = []
    meta = []
    for p in paths:
        text = load_any(p)
        chunks = chunk_text(text)
        for idx, ch in enumerate(chunks):
            all_chunks.append(ch)
            meta.append({
                "source": source_label or os.path.basename(p),
                "path": p,
                "chunk_id": idx,
                "text": ch
            })
    return {"chunks": all_chunks, "meta": meta}
