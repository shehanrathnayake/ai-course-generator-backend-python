from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import course

app = FastAPI()

# Allow frontend origin
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(course.router, prefix="/api/v1")

