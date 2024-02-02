from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse
from sqlalchemy import select, func, or_, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.engine.result import ChunkedIteratorResult  

from app.databases.db_connect import db_session
from app.databases.models import Commodity, CommodityCategory, CommodityBrand
from app.databases.schemas import ReturnData, ReturnHotCommodityData, CommodityQueryCondition,PaginationData

router = APIRouter()


@router.get("/list", response_model=PaginationData, status_code=status.HTTP_200_OK, summary="商品分页")
async def commodity_list(
    query: CommodityQueryCondition = Depends(), dbs: AsyncSession = Depends(db_session)
):
    """商品分页列表以及搜索"""
    query_sql: str = (
        select(Commodity)
        .where(Commodity.delete_time == None,
                query.brand_id == None or Commodity.brand_id == query.brand_id, 
                query.category_id == None or Commodity.category_id == query.category_id ,
                query.title == None or Commodity.title .like(func.concat('%',query.title,'%'))
               )
        .order_by(Commodity.id.desc())
        .offset(query.page_size * (query.per_page - 1))  
        # 需要丢弃的数据，拿到对应页数的数据
        .limit(query.page_size)
    )
    print(query_sql,query.brand_id,query.category_id,query.title,
        #   Commodity.category_id=="${query.category_id}"or""=="",
          )
    datas: ChunkedIteratorResult = await dbs.execute(query_sql)
    count_sql: str = select(func.count(Commodity.id)).where(
        Commodity.delete_time == None
    )
    counts: ChunkedIteratorResult = await dbs.execute(count_sql)
    # return JSONResponse({
    #         "per_page": query.per_page,
    #         "page_size": query.page_size,
    #         "total": counts.scalar(),
    #         "datas": datas.scalars().all(),
    #     }, status_code=status.HTTP_200_OK)
    return {
        "code": status.HTTP_200_OK,
        "per_page": query.per_page,
        "page_size": query.page_size,
        "total": counts.scalar(),
        "datas": datas.scalars().all(),
        "message": "success",
    }

@router.get('/commodity_info', response_model=ReturnData, status_code=status.HTTP_200_OK, summary='商品详情')
async def commodity_info(id: int = Query(title='商品ID'), dbs: AsyncSession = Depends(db_session)):
    """商品详情"""
    query_sql: str = select(Commodity).where(Commodity.delete_time == None, Commodity.id == id)
    result_data: ChunkedIteratorResult = await dbs.execute(query_sql)
    print(query_sql)
    # data = result_data.scalar()
    # data = data.to_dict()
    return{
        "code": status.HTTP_200_OK,
        "data": result_data.scalar(),
        "message": "success",
    }

# @router.get('/key_list', response_model=ReturnData, status_code=status.HTTP_200_OK, summary='检索到的商品')
# async def commodity_info(query: CommodityQueryCondition = Depends(),dbs: AsyncSession = Depends(db_session)):
#     """查询数据"""
#     datas = await Session.query(Commodity).filter(
#         or_(Commodity.category_id == query.category_id, query.category_id == None),
#         or_( Commodity.brand_id== query.brand_id, query.category_id == None),
#         or_(Commodity.title == query.title, query.category_id == None)
#     ).all()
#     # data = result_data.scalar()
#     # data = data.to_dict()
#     count_sql: str = select(func.count(Commodity.id)).where(
#         Commodity.delete_time == None
#     )
#     counts = await Session.query(Commodity).filter(
#         Commodity.delete_time == None
#     ).count
#     return{
#         "code": status.HTTP_200_OK,
#         "per_page": query.per_page,
#         "page_size": query.page_size,
#         "total": counts.scalar(),
#         "datas": datas.scalars().all(),
#         "message": "success",
#     }

@router.get('/hot', response_model=ReturnHotCommodityData, status_code=status.HTTP_200_OK, summary='热门')
async def commodity_hot(dbs: AsyncSession = Depends(db_session)):
    """热门"""
    query_sql: str = select(Commodity).where(Commodity.delete_time == None, Commodity.is_hot == 1).order_by(Commodity.id.asc())
    result_data: ChunkedIteratorResult = await dbs.execute(query_sql)
    # data = result_data.scalars()
    # data = [item.to_dict() for item in data] 
    return {
        "code": status.HTTP_200_OK,
        "data": result_data.scalars().all(),
        "message": "success"
    }

@router.get('/recommend', response_model=ReturnHotCommodityData, status_code=status.HTTP_200_OK, summary='推荐')
async def commodity_recommend(dbs: AsyncSession = Depends(db_session)):
    """推荐"""
    query_sql: str = select(Commodity).where(Commodity.delete_time == None, Commodity.is_recommend == 1).order_by(Commodity.id.asc())
    result_data: ChunkedIteratorResult = await dbs.execute(query_sql)
    # data = result_data.scalars()
    # data = [item.to_dict() for item in data] 
    return {
        "code": status.HTTP_200_OK,
        "data": result_data.scalars().all(),
        "message": "success"
    }
@router.get("/category", response_model=ReturnData, status_code=status.HTTP_200_OK, summary='商品分类')
async def commodity_category(dbs: AsyncSession = Depends(db_session)):
    """商品分类"""
    query_sql: str = select(CommodityCategory).where(CommodityCategory.delete_time == None).order_by(CommodityCategory.id.asc())
    result_data: ChunkedIteratorResult = await dbs.execute(query_sql)

    return {
        "code": status.HTTP_200_OK,
        "data": result_data.scalars().all(),
        "message": "success",
    }

@router.get('/brand', response_model=ReturnData, status_code=status.HTTP_200_OK, summary='商品品牌')
async def commodity_brand(dbs: AsyncSession = Depends(db_session)):
    """商品品牌"""
    query_sql: str = select(CommodityBrand).where(CommodityBrand.delete_time == None).order_by(CommodityBrand.id.desc())
    result_data: ChunkedIteratorResult = await dbs.execute(query_sql)
    return {
        "code": status.HTTP_200_OK,
        "data": result_data.scalars().all(),
        "message": "success",       
    }