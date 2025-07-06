import google.generativeai as genai
from app.services.base_llm_service import BaseLLMService
from app.core.config import settings

class GeminiService(BaseLLMService):
    def __init__(self):
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    async def generate_outline(self, topic: str) -> str:
        prompt = f"Create a mini-course outline on the topic: {topic}. Include sections and lessons."
        response = self.model.generate_content(prompt)
        return response.text
