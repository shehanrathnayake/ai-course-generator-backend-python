from abc import ABC, abstractmethod

class BaseLLMService(ABC):
    @abstractmethod
    async def generate_outline(self, topic: str) -> str:
        pass
