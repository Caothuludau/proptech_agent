from sentence_transformers import SentenceTransformer
import numpy as np

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("intfloat/multilingual-e5-base")
    return _model

# Why this model?
# Good multilingual performance (English + Vietnamese)
# Stable
# No API dependency

def embed_chunks(chunks):
    model = get_model()
    embeddings = model.encode(
        chunks,
        normalize_embeddings=True,
        batch_size=32
    )
    print(embeddings.shape)
    return embeddings