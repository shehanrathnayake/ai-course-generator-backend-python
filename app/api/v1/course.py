from fastapi import APIRouter, HTTPException, Depends
from app.models.course import CourseOutlineRequest, CourseOutlineResponse
from app.services.gemini_service import GeminiService
from app.services.base_llm_service import BaseLLMService

router = APIRouter()

# Dependency injection provider function
def get_llm_service() -> BaseLLMService:
    # Here we return GeminiService, but in the future
    # we could swap to another implementation (e.g., OpenAIService)
    return GeminiService()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post("/generate-outline", response_model=CourseOutlineResponse)
async def generate_outline(
    request: CourseOutlineRequest,
    llm_service: BaseLLMService = Depends(get_llm_service)
):
    try:
        outline = await llm_service.generate_outline(request.topic)
        return CourseOutlineResponse(outline=outline)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
