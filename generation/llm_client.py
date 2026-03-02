from google import genai

class LLMClient:

    def __init__(self, model_name="gemini-2.0-flash"):
        self.model_name = model_name
        # Client sẽ tự động tìm biến môi trường GOOGLE_API_KEY
        self.client = genai.Client()

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )
        
        return response.text