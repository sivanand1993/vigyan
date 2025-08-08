import os
import faiss
import pickle
from typing import List, Dict, Any, Tuple
import numpy as np

INDEX_PATH = os.path.join("storage", "index.faiss")
STORE_PATH = os.path.join("storage", "store.pkl")

def load_index() -> Tuple[faiss.IndexFlatIP, list]:
    if not (os.path.exists(INDEX_PATH) and os.path.exists(STORE_PATH)):
        return None, []
    index = faiss.read_index(INDEX_PATH)
    with open(STORE_PATH, "rb") as f:
        store = pickle.load(f)
    return index, store

def save_index(index: faiss.IndexFlatIP, store: list):
    os.makedirs("storage", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    with open(STORE_PATH, "wb") as f:
        pickle.dump(store, f)

def build_index(embeddings: np.ndarray, meta: list):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # cosine if inputs are normalized
    index.add(embeddings.astype("float32"))
    save_index(index, meta)

def add_to_index(embeddings: np.ndarray, meta: list):
    index, store = load_index()
    if index is None:
        build_index(embeddings, meta)
        return
    index.add(embeddings.astype("float32"))
    store.extend(meta)
    save_index(index, store)

def search(query_emb: np.ndarray, top_k: int = 5) -> List[Dict[str, Any]]:
    index, store = load_index()
    if index is None:
        return []
    D, I = index.search(query_emb.astype("float32"), top_k)
    results = []
    for score, idx in zip(D[0], I[0]):
        if idx < 0 or idx >= len(store):
            continue
        item = store[idx].copy()
        item["score"] = float(score)
        results.append(item)
    return results
