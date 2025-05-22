from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas.response import ResponseModel
from app.core.logger import logger


async def http_exception_handler(_request: Request, exc: HTTPException):
    logger.error(f"HTTPException: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=ResponseModel(success=False, message=exc.detail).dict()
    )


async def validation_exception_handler(_request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content=ResponseModel(
            success=False, message="Validation error", data=exc.errors()).dict()
    )


async def general_exception_handler(_request: Request, _exc: Exception):
    logger.exception("Unhandled error")
    return JSONResponse(
        status_code=500,
        content=ResponseModel(
            success=False, message="Internal server error").dict()
    )
