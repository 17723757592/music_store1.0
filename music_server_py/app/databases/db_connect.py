from typing import Callable, AsyncGenerator
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

__all__ = ['db_session']

_SQLALCHEMY_DATABASE_URL = 'mysql+aiomysql://root:123456@127.0.0.1:3306/music_shop?charset=utf8mb4'
# 初始化数据库连接
_engine_async = create_async_engine(_SQLALCHEMY_DATABASE_URL, pool_use_lifo=True, pool_pre_ping=True, pool_size=5, pool_recycle=100)
# 创建session元类
async_session_local: Callable[..., AsyncSession] = sessionmaker(
    bind=_engine_async,
    class_=AsyncSession,    
    autoflush=False,
    autocommit=False
)

# 构建模型基类
# BaseModel = declarative_base()    
# BaseModel.metadata.create_all(bind=_engine)


async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """异步生成器，作为Depends的选项"""
    async with async_session_local() as session:  
        # 实例化
        try:
            yield session
        finally:
            await session.close()