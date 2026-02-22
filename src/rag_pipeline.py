query = "termination clause"
query_embedding = model.encode(
    [query],
    normalize_embeddings=True
)

D, I = index.search(
    np.array(query_embedding).astype("float32"),
    k=3
)

for idx in I[0]:
    print("------")
    print(chunks[idx])