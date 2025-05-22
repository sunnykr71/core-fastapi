from fastapi import APIRouter
from app.schemas.response import ResponseModel
from app.core.logger import logger

router = APIRouter()


@router.get("/", response_model=ResponseModel)
async def health_check():

    logger.info("Health check requested")

    health_data = {
        "status": "healthy",
        "environment": "development"
    }

    return ResponseModel(
        success=True,
        message="Health check successful",
        data=health_data
    )
