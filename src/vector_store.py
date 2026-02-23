from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from qdrant_client.models import PointStruct

def init_collection(collection_name, dimension, client=None):
    if client is None:
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
    if chunks is None or embeddings is None:
        raise ValueError("Chunks and embeddings must be provided and cannot be empty.")
    if len(chunks) == 0 or len(embeddings) == 0:
        raise ValueError("Chunks and embeddings must be provided and cannot be empty.")
    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings must have the same length.")
        
    points = [
        PointStruct(
            id=i,
            vector=embeddings[i].tolist(),
            payload={"text": chunks[i]}
        )
        for i in range(len(chunks))
    ]

    client.upsert(
        collection_name=collection_name,
        points=points
    )


def search_collection(client, collection_name, query_vector, limit=3):
    """Search the collection for nearest vectors.

    Tries to use the client.search API if available; otherwise falls back
    to the Qdrant HTTP endpoint on localhost:6333.
    """
    # Prefer client.search when available
    if hasattr(client, "search"):
        return client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=limit,
            with_payload=True,
        )

    # Fallback: use HTTP API (assumes local Qdrant on port 6333)
    import requests
    from types import SimpleNamespace

    url = f"http://localhost:6333/collections/{collection_name}/points/search"
    payload = {"vector": query_vector, "limit": limit, "with_payload": True}
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    body = resp.json()

    results = []
    for item in body.get("result", []):
        results.append(SimpleNamespace(score=item.get("score"), payload=item.get("payload", {})))

    return results