from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("intfloat/multilingual-e5-base")

# Why this model?
# Good multilingual performance (English + Vietnamese)
# Stable
# No API dependency

embeddings = model.encode(
    chunks,
    normalize_embeddings=True
)

print(embeddings.shape)