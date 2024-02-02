from sqlalchemy.orm.decl_api import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    INTEGER,
    VARCHAR,
    DATETIME,
    TEXT,
    SMALLINT,
    DECIMAL,
    CHAR,
    func,
)
# 创建一个基类（DeclarativeBase：陈述的，声明式）
BaseModel: DeclarativeBase = declarative_base()


class BaseFieldModel(BaseModel):
    """公共字段"""

    __abstract__ = True
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    create_time = Column(DATETIME, nullable=False, default=func.now())
    update_time = Column(DATETIME, nullable=False, default=func.now(), onupdate=func.now())
    delete_time = Column(DATETIME, nullable=True)


class CommodityBrand(BaseFieldModel):
    """商品品牌"""

    __tablename__ = "commodity_brand"
    title = Column(VARCHAR(30), nullable=False, comment="标题")


class CommodityCategory(BaseFieldModel):
    """商品分类"""

    __tablename__ = "commodity_category"
    title = Column(VARCHAR(50), nullable=False, comment="标题")
    ico = Column(VARCHAR(30), nullable=False, comment="图标")
    name = Column(VARCHAR(50), nullable=False, comment="路由name")


class Commodity(BaseFieldModel):
    """商品"""

    __tablename__ = "commodity"
    title = Column(VARCHAR(100), nullable=False, comment="商品名称")
    quantity = Column(
        INTEGER, nullable=False, default="0", server_default="0", comment="商品数量"
    )
    price = Column(
        DECIMAL(8, 2),
        nullable=False,
        default="0.00",
        server_default="0.00",
        comment="价格",
    )
    show_picture = Column(VARCHAR(225), nullable=False, comment="图片")
    brand_id = Column(INTEGER, nullable=False, comment="品牌ID")
    category_id = Column(INTEGER, nullable=False, comment="分类ID")
    pictures = Column(TEXT, nullable=False, comment="图册")
    is_hot = Column(
        SMALLINT,
        nullable=False,
        default="0",
        server_default="0",
        comment="是否热门商品 0:否 1:是",
    )
    is_recommend = Column(
        SMALLINT,
        nullable=False,
        default="0",
        server_default="0",
        comment="是否推荐 0:否 1:是",
    )
    sales_volume = Column(
        INTEGER, nullable=False, default="0", server_default="0", comment="销量"
    )
    views = Column(
        INTEGER, nullable=False, default="0", server_default="0", comment="浏览量"
    )
    content = Column(TEXT, comment="内容详情")
    discount = Column(VARCHAR(20), comment="优惠")
    standard = Column(VARCHAR(20), nullable=False, comment="商品规格")
    # def to_dict1(self):
    #         return dict(title = self.title, quantity = self.quantity, pictures = self.pictures, 
    #                     brand_id = self.brand_id, category_id = self.category_id, is_hot = self.is_hot,
    #                     is_recommend = self.is_recommend, sales_volume = self.sales_volume,
    #                     views = self.views, content = self.content, id = self.id, price = self.price,
    #                     create_time =self.create_time, update_time = self.update_time,
    #                     delete_time = self.delete_time, show_picture = self.show_picture)


class Banner(BaseFieldModel):
    """banner图"""

    __tablename__ = "banner"
    title = Column(VARCHAR(60), nullable=False, comment="标题")
    picture = Column(VARCHAR(225), nullable=False, comment="图片")
    url = Column(VARCHAR(225), comment="图片关联链接")
    bgc = Column(VARCHAR(225), comment="图片背景色")


class User(BaseFieldModel):
    """用户"""

    __tablename__ = "user"
    username = Column(VARCHAR(20), nullable=False, comment="登录账号")
    password = Column(VARCHAR(100), nullable=False, comment="密码")
    nickname = Column(VARCHAR(20), comment="昵称")      
    avatar = Column(VARCHAR(225), comment="头像")
    phone = Column(VARCHAR(11), comment="手机号")


class UserAddress(BaseFieldModel):
    """用户地址"""

    __tablename__ = "user_address"
    u_id = Column(VARCHAR(20), nullable=False, comment="用户ID")
    contact_personnel = Column(VARCHAR(20), nullable=False, comment="收件人")
    contact_phone = Column(VARCHAR(11), nullable=False, comment="联系电话")
    address = Column(VARCHAR(225), nullable=False, comment="收件地址")
    id_default = Column(
        SMALLINT,
        nullable=False,
        default="0",
        server_default="0",
        comment="是否默认地址 0:否 1:是",
    )


class Order(BaseFieldModel):
    """商品订单"""

    __tablename__ = "order"
    order_sn = Column(CHAR(16), nullable=False, comment="订单号")
    u_id = Column(VARCHAR(20), nullable=False, comment="用户ID")    
    status = Column(SMALLINT, nullable=False, comment="订单状态 1:待付款 2:待发货 3:待收货 4:已完成")
    pay_price = Column(
        DECIMAL(10, 2),
        nullable=False,
        default="0.00",
        server_default="0.00",
        comment="支付价格",
    )
    pay_type = Column(SMALLINT, nullable=False, comment="支付方式 1:支付宝 2:微信")
    pay_sn = Column(CHAR(16), comment="支付单号")
    is_payment = Column(
        SMALLINT,
        nullable=False,
        default="0",
        server_default="0",
        comment="是否支付 0:否 1:是",
    )
    pay_time = Column(DATETIME, comment="支付时间")
    contact_personnel = Column(VARCHAR(20), nullable=False, comment="收件人")
    contact_phone = Column(VARCHAR(11), nullable=False, comment="联系电话")
    address = Column(VARCHAR(225), nullable=False, comment="收件地址")


class OrderCommodity(BaseFieldModel):
    """订单商品"""

    __tablename__ = "order_commodity"   
    order_id = Column(CHAR(16), nullable=False, comment="订单ID")   
    u_id = Column(VARCHAR(20), nullable=False, comment="用户ID")
    commodity_id = Column(INTEGER, nullable=False, comment="商品ID")
    title = Column(VARCHAR(100), nullable=False, comment="商品名称")
    price = Column(
        DECIMAL(8, 2),
        nullable=False,
        default="0.00",
        server_default="0.00",
        comment="购买价格",
    )
    brand_id = Column(INTEGER, nullable=False, comment="品牌ID")
    category_id = Column(INTEGER, nullable=False, comment="分类ID")
    pictures = Column(TEXT, nullable=False, comment="图册")
    quantity = Column(INTEGER, nullable=False, comment="购买数量")


class Conservator(BaseFieldModel):
    """管理员"""

    __tablename__ = "conservator"
    username = Column(VARCHAR(20), nullable=False, comment="登录账号")
    password = Column(VARCHAR(100), nullable=False, comment="密码")
    nickname = Column(VARCHAR(20), comment="昵称")
    avatar = Column(VARCHAR(225), comment="头像")


if __name__ == "__main__":
    from sqlalchemy import create_engine

    _engine = create_engine(
        "mysql+pymysql://root:123456@localhost:3306/music_shop?charset=utf8mb4"
    )
    BaseModel.metadata.create_all(_engine)
    #创建表，执行所有BaseModel类的子类

    # def to_dict(self):
    #     return dict(title = self.title, picture = self.picture, url = self.url,
    #                 id = self.id, create_time =self.create_time, update_time = self.update_time,
    #                 delete_time = self.delete_time, bgc = self.bgc)
