from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

def init_collection(collection_name, dimension):
    client = QdrantClient("localhost", port=6333)

    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=dimension,
            distance=Distance.COSINE
        ),
    )

    return client

def upsert_embeddings(client, collection_name, chunks, embeddings):
    if not chunks or not embeddings:
        raise ValueError("Chunks and embeddings must be provided and cannot be empty.")
        
    points = [
        {
            "id": i,
            "vector": embeddings[i].tolist(),
            "payload": {
                "text": chunks[i],
                "source": "lease_contract_01",
            }
        }
        for i in range(len(chunks))
    ]

    client.upsert(
        collection_name=collection_name,
        points=points
    )