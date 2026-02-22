from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient("localhost", port=6333)

dimension = embeddings.shape[1]

client.recreate_collection(
    collection_name="lease_chunks",
    vectors_config=VectorParams(
        size=dimension,
        distance=Distance.COSINE
    ),
)

points = [
    {
        "id": i,
        "vector": embeddings[i].tolist(),
        "payload": {
            "text": chunks[i],
            "source": "lease_contract_01",
        },
    }
    for i in range(len(chunks))
]

client.upsert(
    collection_name="lease_chunks",
    points=points
)