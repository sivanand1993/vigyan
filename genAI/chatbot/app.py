import os
import streamlit as st
from openai import OpenAI
from embed import prepare_docs, embed_texts
from search import add_to_index, search

st.set_page_config(page_title="Ask My Data — Mini RAG", page_icon="📄", layout="wide")
st.title("📄 Ask My Data — Mini RAG (Streamlit + FAISS)")

with st.sidebar:
    st.header("📤 Upload & Index")
    uploaded_files = st.file_uploader("Upload TXT, PDF, DOCX files", type=["txt", "pdf", "docx"], accept_multiple_files=True)
    build_clicked = st.button("🔨 Build / Update Index")
    st.caption("Set OPENAI_API_KEY in your environment before running.")

def persist_uploads(files):
    saved_paths = []
    if not files:
        return saved_paths
    os.makedirs("data", exist_ok=True)
    for f in files:
        path = os.path.join("data", f.name)
        with open(path, "wb") as out:
            out.write(f.read())
        saved_paths.append(path)
    return saved_paths

if build_clicked:
    if not uploaded_files:
        st.warning("Please upload at least one file.")
    else:
        with st.spinner("Reading & embedding..."):
            paths = persist_uploads(uploaded_files)
            prepared = prepare_docs(paths)
            embeddings = embed_texts(prepared["chunks"])
            add_to_index(embeddings, prepared["meta"])
        st.success(f"Indexed {len(prepared['chunks'])} chunks from {len(paths)} file(s).")

st.subheader("💬 Ask a question about your files")
query = st.text_input("Your question")

def answer_with_citations(question: str, top_k: int = 5):
    from search import load_index
    idx, store = load_index()
    if idx is None:
        return "No index found. Upload files and build index first.", []
    q_emb = embed_texts([question])
    hits = search(q_emb, top_k=top_k)
    context = "\n\n---\n\n".join([f"[Source: {h['source']} | chunk {h['chunk_id']}]\n{h['text']}" for h in hits])
    sys = "You are a helpful assistant that answers based on the provided context only, with citations."
    user = f"Question: {question}\n\nContext:\n{context}"
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "system", "content": sys}, {"role": "user", "content": user}], temperature=0.2)
    return resp.choices[0].message.content, hits

if st.button("🧠 Get Answer"):
    if not query.strip():
        st.warning("Please type a question first.")
    else:
        with st.spinner("Thinking..."):
            ans, hits = answer_with_citations(query, top_k=5)
        st.markdown("### Answer")
        st.write(ans)
        if hits:
            st.markdown("### Retrieved Chunks")
            for h in hits:
                with st.expander(f"{h['source']} — chunk {h['chunk_id']} (score={h['score']:.3f})"):
                    st.write(h["text"])