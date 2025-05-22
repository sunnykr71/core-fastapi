from fastapi import FastAPI
from app.api.v1.router import api_router as v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "message": "Hello World"
    }
