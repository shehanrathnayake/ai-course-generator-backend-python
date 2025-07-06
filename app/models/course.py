from pydantic import BaseModel

class CourseOutlineRequest(BaseModel):
    topic: str

class CourseOutlineResponse(BaseModel):
    outline: str
