from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.exceptions import HTTPException
from app.logger import logger


async def register_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handle(request: Request, exc: RequestValidationError):
        """客户端请求参数错误"""
        await logger.error("HTTP-CODE: 422 | REQUEST-DATA: {}".format(str(request.body())))
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            content=jsonable_encoder({"code": 422, "message": str(exc)})
        )

    @app.add_exception_handler(HTTPException)
    async def http_exception_handle(request: Request, exc: HTTPException):
        """http服务错误"""

        await logger.error(
            "HTTP-CODE: {} | HTTP-ERR: {} | REQUEST-DATA: {}".format(
                exc.status_code, str(exc.detail), str(request.body())
            )
        )
        return JSONResponse(
            status_code=200,
            content={"code": exc.status_code, "message": str(exc.detail)},
        )
