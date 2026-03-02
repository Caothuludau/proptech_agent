class PromptBuilder:

    @staticmethod
    def build_qa_prompt(context: str, question: str) -> str:
        return f"""
        You are a legal assistant specialized in lease agreements.

        Answer strictly using the context below.
        If the answer is not present, say "Not found in document."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """