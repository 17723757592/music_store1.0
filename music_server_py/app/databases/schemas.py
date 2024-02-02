from typing import Union, Optional, List, Dict
from fastapi import Query
from pydantic import BaseModel, Field


class PageSchemes(BaseModel):
    """分页器"""

    per_page: int = Query(title="页码", default=1, gt=0)
    page_size: int = Query(title="每页数量", default=10, gt=0)


class CommodityQueryCondition(PageSchemes):
    """商品分页查询条件"""

    title: Optional[str] = Query(default=None, title="商品名称", description="商品名称")
    brand_id: Optional[int] = Query(default=None, title="品牌", description="品牌")
    category_id: Optional[int] = Query(default=None, title="分类", description="分类")
    # price: tuple = Query(default=None, title="价格区间", description="价格区间")
        
    class Config:
        orm_mode = True

class CommodityBack(BaseModel):
    """商品响应对象"""

    id: int = Field(title="商品ID", description="商品唯一标识")
    title: str = Field(title="商品名称")
    quantity: int = Field(title="数量")
    price: float = Field(title="价格")
    brand_id: int = Field(title="品牌ID")
    category_id: int = Field(title="分类ID")
    show_picture: str = Field(title="图片地址")
    pictures: str = Field(title="图册")
    is_hot: int = Field(title="是否热门", description="1是 0否")
    is_recommend: int = Field(title="是否推荐", description="1是 0否")
    sales_volume: int = Field(title="销量")
    views: int = Field(title="浏览量")
    content: str = Field(title="商品描述")
    discount:str = Field(title="商品折扣")
    standard:str = Field(title="商品规格")
    # 启用orm模式
    class Config:
        orm_mode = True

class UserBack(BaseModel):
    """用户对象模型"""
    username: str = Field(title="登录账号")
    nickname: str = Field(title="昵称")
    phone: str = Field(title="手机号码")
    id: int = Field(title="id")
    avatar: Optional[str] = Field(title="头像")

    class Config:
        orm_mode = True

class UserInDB(UserBack):
    hashed_password: str = Field(title="数据库存储密码")  

class UserInput(UserBack):
    password: str = Field(title="用户输入密码")

class addOrderCommodity(BaseModel):
    """储存订单商品模型"""
    order_id : str = Field(title="订单ID")
    u_id :str = Field(title="用户ID")
    commodity_id :int = Field(title="商品ID")
    title :str = Field(title="商品名称")
    price :float = Field(title="商品单价")
    brand_id :int = Field(title="品牌ID")
    category_id :int = Field(title="分类ID")
    pictures :str = Field(title="图片")
    quantity :int = Field(title="数量")

class Token(BaseModel):
    """"令牌响应数据模型"""

    access_token: str 
    token_type: str 

class TokenData(BaseModel):
    username:Union[str, None] = None

class RefreshToken(BaseModel):
    refresh_token: str

# class shopping(BaseModel):
#     id:int = Field("商品编号")
#     pictures:str = Field("商品图片")
#     quantity:int = Field("商品数量")
#     price:str = Field("商品单价")
#     title:str = Field("商品标题")

# class address(BaseModel):
#     address:str = Field(title="收获地址")
#     contact_personnel:str = Field(title="收件人")
#     contact_phone:str = Field(title="联系电话")
#     id:int = Field(title="地址id")


class orderInformation(BaseModel):
    """订单模型"""

    order_sn:int = Field(title="订单号")
    u_id :str = Field(title="用户ID")
    pay_price:float = Field(title="订单应付金额")
    contact_personnel:str = Field(title="收件人")
    contact_phone:str = Field(title="联系电话")
    address:str = Field(title="收获地址")


class BannerBack(BaseModel):
    """banner图"""
    id: int = Field(title="商品ID", description="商品唯一标识")
    title: str = Field(title="标题")
    picture: str = Field(title="图片地址")
    bgc:str = Field(title = '背景色')
    url: str = Field(title="链接地址")

    class Config:
        orm_mode = True


class CategoryBack(BaseModel):
    """分类"""

    id: int = Field(title='分类id')
    ico: str = Field(title='图标')
    title: str = Field(title='标题')
    name: str = Field(title='路由name')

    class Config:
        orm_mode = True
    

class BrandBack(BaseModel):
    """品牌"""

    title: str = Field(title='标题')

    class Config:
        orm_mode = True


class PaginationData(BaseModel):
    """分页结构"""
    code: int = Field(title="请求状态码")
    per_page: int = Field(title="页码")
    page_size: int = Field(title="分页数量")
    total: int = Field(title="总数")
    datas: Optional[List[CommodityBack]] = Field(None, title="数据")
    message: str = Field(title="提示信息")


class ReturnData(BaseModel):
    """响应数据结构"""

    code: int = Field(title="请求状态码")
    data: Union[PaginationData, CommodityBack, List[CommodityBack],List[UserBack],List[BannerBack], List[CategoryBack], list, None] = Field(None, title="数据")
    message: str = Field(title="提示信息")
# data会在union中找到合适的模型，月详细的模型应该放在越前面

class ReturnHotCommodityData(BaseModel):
    """响应数据结构"""

    code: int = Field(title="请求状态码")
    data: Optional[List[CommodityBack]] = Field(None, title="数据")
    message: str = Field(title="提示信息")