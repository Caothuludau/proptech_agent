from src.chunking import chunk_document
from src.embedding import embed_chunks
from src.vector_store import init_collection, upsert_embeddings, search_collection
from qdrant_client import QdrantClient
from src.parser import load_pdf

class RAGPipeline:

    def __init__(self, collection_name="lease_chunks"):
        self.collection_name = collection_name
        self.client = QdrantClient("localhost", port=6333)
        
    def ingest(self, pdf_path):
        print("Loading PDF...")
        text = load_pdf(pdf_path)

        print("Chunking...")
        chunks = chunk_document(text, chunk_size=1000, chunk_overlap=200)
        print(f"Total chunks: {len(chunks)}")

        print("Embedding...")
        embeddings = embed_chunks(chunks)

        print("Initializing vector store...")
        self.client = init_collection(
            self.collection_name,
            dimension=len(embeddings[0]),
            client=self.client
            )
        
        upsert_embeddings(
            self.client, 
            self.collection_name, 
            chunks, 
            embeddings
            )
        
        print("Pipeline completed.")
        pass

    def query(self, question, top_k=3):

        query_embedding = embed_chunks([question])[0]

        results = search_collection(
            self.client,
            collection_name=self.collection_name,
            query_vector=query_embedding.tolist(),
            limit=top_k,
        )

        for r in results:
            print("Score:", r.score)
            print("------")
            print("RAW PAYLOAD:", r.payload["text"])
