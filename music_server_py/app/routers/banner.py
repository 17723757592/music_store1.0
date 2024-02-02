from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine.result import ChunkedIteratorResult

from app.databases.db_connect import db_session
from app.databases.models import Banner
from app.databases.schemas import ReturnData
from app.logger import logger

router = APIRouter()

@router.get("/list", response_model=ReturnData, status_code=status.HTTP_200_OK)
async def get_banner(dbs: AsyncSession = Depends(db_session)):
    """banner列表"""
    query_sql: str = select(Banner).where(Banner.delete_time == None).order_by(Banner.id.asc())
    result_datas: ChunkedIteratorResult = await dbs.execute(query_sql)
    print(query_sql)
    # logger.info(result_datas.scalars().all())
    # 游标，all()后下标指向空，若执行上一步，则return中的data会为空
    # while True:
    #     data = result_datas.fetchone()
    #     if not data:
    #         break
    
    return {
        "code": status.HTTP_200_OK,
        "data": result_datas.scalars().all(),
        "message": "success",
    }