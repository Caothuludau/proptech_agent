from src.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()
pipeline.ingest("./data/VA Parking Lease Agreement.pdf")
