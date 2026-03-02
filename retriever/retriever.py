from embeddings import embedding
from vectorstore import vector_store

class Retriever:

    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, question: str, top_k: int = 3):
        # 1. Embed query
        query_vector = self.embedder.encode([question])[0]

        # 2. Search vector DB
        results = self.vector_store.search(
            query_vector=query_vector,
            top_k=top_k
        )

        return results