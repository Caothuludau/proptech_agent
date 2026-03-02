import os
import sys

# Ensure project root is on sys.path so top-level packages like `core` are importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
	sys.path.insert(0, PROJECT_ROOT)

from core.rag_pipeline import RAGPipeline


def main():
	pipeline = RAGPipeline()
	# pipeline.ingest("./data/VA Parking Lease Agreement.pdf")

	question = "What is the duration of the lease agreement?"
	response = pipeline.answer(question)

	# Print response content in a few common formats
	if hasattr(response, "text"):
		print(response.text)
	elif isinstance(response, dict) and "text" in response:
		print(response["text"])
	else:
		print(response)


if __name__ == "__main__":
	main()