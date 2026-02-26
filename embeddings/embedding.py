from sentence_transformers import SentenceTransformer
import numpy as np
from typing import Iterable, List
from core.config import EMBEDDING_MODEL_NAME, EMBEDDING_BATCH_SIZE


class Embedder:
    """Embedding service that lazily loads a SentenceTransformer model.

    Usage:
        embedder = Embedder("intfloat/multilingual-e5-base")
        embeddings = embedder.embed_chunks(chunks)
    """

    def __init__(self, model_name: str = EMBEDDING_MODEL_NAME, batch_size: int = EMBEDDING_BATCH_SIZE):
        self.model_name = model_name
        self.batch_size = batch_size
        self._model = None

    def _load_model(self):
        if self._model is None:
            self._model = SentenceTransformer(self.model_name)
        return self._model

    def embed_chunks(self, chunks: Iterable[str], normalize: bool = True) -> np.ndarray:
        model = self._load_model()
        embeddings = model.encode(
            list(chunks),
            normalize_embeddings=normalize,
            batch_size=self.batch_size,
        )
        print(getattr(embeddings, "shape", None))
        return embeddings


# Module-level default embedder for convenience (keeps previous API)
_default_embedder = Embedder()


def get_embedder() -> Embedder:
    """Return the default Embedder instance."""
    return _default_embedder


def embed_chunks(chunks: Iterable[str]) -> np.ndarray:
    """Compatibility wrapper that uses the default embedder."""
    return _default_embedder.embed_chunks(chunks)