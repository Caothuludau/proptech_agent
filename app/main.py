import os
import sys

# Ensure project root is on sys.path so top-level packages like `core` are importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
	sys.path.insert(0, PROJECT_ROOT)

from core.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()
pipeline.ingest("./data/VA Parking Lease Agreement.pdf")
pipeline.query("What is the duration of the lease agreement?")