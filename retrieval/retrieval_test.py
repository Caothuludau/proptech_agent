query = "Under what conditions can the tenant terminate the lease?"

query_embedding = model.encode(
    [query],
    normalize_embeddings=True
)

results = client.search(
    collection_name="lease_chunks",
    query_vector=query_embedding[0],
    limit=3
)

for r in results:
    print("Score:", r.score)
    print(r.payload["text"])
    print("------")