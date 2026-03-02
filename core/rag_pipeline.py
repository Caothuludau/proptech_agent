from generation.llm_client import LLMClient
from generation.prompt_builder import PromptBuilder
from ingestion.chunking import chunk_document
from embeddings.embedding import embed_chunks
from vectorstore.vector_store import init_collection, upsert_embeddings, search_collection
from qdrant_client import QdrantClient
from ingestion.parser import load_pdf
from core.config import DEFAULT_COLLECTION_NAME, QDRANT_HOST, QDRANT_PORT

class RAGPipeline:

    def __init__(self, 
                 collection_name: str = DEFAULT_COLLECTION_NAME, 
                 llm_client=None):
        self.collection_name = collection_name
        self.client = QdrantClient(QDRANT_HOST, port=QDRANT_PORT)
        if llm_client is None:
            self.llm_client = LLMClient()
        elif isinstance(llm_client, LLMClient):
            self.llm_client = llm_client
        elif callable(llm_client):
            self.llm_client = llm_client()
        else:
            self.llm_client = llm_client

        
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

        return search_collection(
            self.client,
            collection_name=self.collection_name,
            query_vector=query_embedding.tolist(),
            limit=top_k,
        )

        # for r in results:
        #     print("Score:", r.score)
        #     print("------")
        #     print("RAW PAYLOAD:", r.payload["text"])

    def answer(self, question: str, top_k=3):

        results = self.query(question, top_k)

        context = "\n\n".join(
            [r.payload["text"] for r in results]
        )

        prompt = PromptBuilder.build_qa_prompt(context, question)

        response = self.llm_client.generate(prompt)

        return response