from fastapi import Depends, APIRouter, status ,HTTPException, Query
from typing import Union, List
from fastapi.responses import JSONResponse
from sqlalchemy import select, delete, update, insert
from sqlalchemy.orm  import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.engine.result import ChunkedIteratorResult
from app.databases.db_connect import db_session, async_session_local
from app.databases.models import User, UserAddress , Order, OrderCommodity
from app.databases.schemas import ReturnData,UserInDB, Token, TokenData, UserBack, UserInput, orderInformation, addOrderCommodity, RefreshToken

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": False,
#     },
# }

SECRET_KEY = "ab09edbbaf1acd6a0131ca0ac3e2f345cbc8ac7a0a93fa84bca18e24290d2025"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 2

router = APIRouter()

# def fake_hash_password(password: str):
#     return "fakehashed" + password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/token")

def get_db():
    db = async_session_local()
    try:
        yield db
    finally:
        db.close()


def get_pwd_hash(pwd):
    return pwd_context.hash(pwd)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def create_db_user(user:UserInput,db:AsyncSession = Depends(db_session)):
    hashed_password = get_pwd_hash(user.password)
    db_user = User(
        username = user.username,password = hashed_password, 
        # avatar = user.avatar, id = user.id,
        # phone = user.phone, nickname = user.nickname,
        create_time = datetime.utcnow(), update_time = datetime.utcnow()
    )
    db.add(db_user)
    await db.commit()
    db.refresh(db_user)
    return db_user

async def get_user(db, username: str):
    query_sql: str = select(User).where(User.delete_time == None,User.username == username).order_by(User.id.asc())
    print(query_sql)
    result_data: ChunkedIteratorResult = await db.execute(query_sql)
    db:UserInDB = result_data.scalar()
    if db:
        return UserInDB(
            username = db.username, 
            hashed_password=db.password, 
            avatar=db.avatar,
            id = db.id, 
            nickname= db.nickname, 
            phone= db.phone
        )
        # return db 
    

async def get_address(db, username: str):
    query_sql: str = select(UserAddress).where(UserAddress.delete_time == None,UserAddress.u_id == username).order_by(UserAddress.id.asc())
    print(query_sql)
    result_data: ChunkedIteratorResult = await db.execute(query_sql)
    data:UserInDB = result_data.scalars().all()
    return {
        "code": status.HTTP_200_OK,
        "data": data,
        "message": "success",       
    }


async def get_commodity(dbs, order_id: str):
    query_sql: str = select(Order).where(Order.delete_time == None, Order.order_sn == order_id)
    result_data: ChunkedIteratorResult = await dbs.execute(query_sql)
    return{
        "code": status.HTTP_200_OK,
        "data": result_data.scalars().all(),
        "message": "success",
    }


async def get_order(db,u_id:str):
    query_sql: str = select(OrderCommodity).where(OrderCommodity.delete_time == None, OrderCommodity.u_id == u_id).order_by(OrderCommodity.update_time.desc())
    # print(query_sql, ordernumber.number)
    result_data: ChunkedIteratorResult = await db.execute(query_sql)
    return{
        "code": status.HTTP_200_OK,
        "data": result_data.scalars().all(),
        "message": "success",
    }

async def authenticate_user(db, username: str, password: str):
    print(username)
    user:UserInDB = await get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_user_from_refresh_token(refresh_token):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token = create_access_token(
    #     data={"sub": username}, expires_delta=access_token_expires
    #     )
    # return {'access_token': access_token, 'token_type': 'bearer'}

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/create")
async def create_user(user:UserInput = Depends() , dbs: AsyncSession = Depends(db_session)):
    """创建用户"""
    query_sql: str = (
        select(User)
        .where(User.delete_time == None, User.username == user.username)
        .order_by(User.id.asc())
    )
    result_data: ChunkedIteratorResult = await dbs.execute(query_sql)
    if result_data.scalar():
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='已存在该用户'
        )
    print(user)
    # return(user)
    return await create_db_user(user, dbs)

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(db_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_user_address(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(db_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    address = await get_address(db, username=token_data.username)
    if address is None:
        raise credentials_exception
    return address


async def get_user_order(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(db_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    order_list = await get_order(db, u_id=token_data.username)
    if order_list is None:
        raise credentials_exception
    return order_list


async def get_order_commodity(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(db_session),order_id: str = Query(title='订单ID')):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    commodity = await get_commodity(db,order_id)
    if commodity is None:
        raise credentials_exception
    return commodity

# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), dbs:  AsyncSession = Depends(db_session)):
    user = await authenticate_user(dbs, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_access_token(
        data={"sub": user.username}, expires_delta=refresh_token_expires
    )
    # return {"access_token": access_token, "token_type": "bearer"}
    return {'access_token': access_token, 'token_type': 'bearer', 'refresh_token': refresh_token}

@router.post("/refresh_token")
def refresh(refresh_token:str):
    username = get_user_from_refresh_token(refresh_token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    # 创建新的访问令牌
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_access_token(
        data={"sub": username}, expires_delta=refresh_token_expires
    )
    # return {"access_token": access_token, "token_type": "bearer"}
    return {'access_token': access_token, 'token_type': 'bearer', 'refresh_token': refresh_token}

@router.get("/me" ,response_model=UserBack, summary="读取用户信息")
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user


@router.get("/address", summary="用户地址")     
async def read_user_address(user_address = Depends(get_user_address)):
    return user_address
    # query_sql:str = (
    #     select(UserAddress)
    #     .where(UserAddress.delete_time == None)
    #     .order_by(UserAddress.id.asc())
    # )
    # result_data:ChunkedIteratorResult = await db.execute(query_sql)
    # return{
    #     "code": status.HTTP_200_OK,
    #     "data": result_data.scalars().all(),
    #     "message": "success"
    # }


@router.get("/commodity", status_code=status.HTTP_200_OK, summary='订单详情')
async def read_order(order_commodity = Depends(get_order_commodity)):
    """获取订单详情"""
    return order_commodity


@router.get("/readOrder", status_code=status.HTTP_200_OK, summary='订单列表')
async def read_order(order_list = Depends(get_user_order)):
    """获取订单列表"""
    return order_list   


@router.post("/order",status_code=status.HTTP_200_OK, summary='储存订单信息')
async def post_order_commodity(order: orderInformation =Depends(), token:str = Depends(oauth2_scheme), db:AsyncSession = Depends(db_session)):
    """储存订单信息"""
    # 这里orderData传入的是orderData的模型，所以后续需要读取属性后与数据库逻辑比较
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    add_order = Order(
        order_sn = order.order_sn,
        u_id  = order.u_id,
        status = 1,
        pay_price = order.pay_price,
        pay_type = 0,
        is_payment = 0,
        contact_personnel=order.contact_personnel,
        contact_phone = order.contact_phone,
        address = order.address,
        create_time = datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),
        update_time = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    )
    db.add(add_order)
    await db.commit()
    await db.refresh(add_order)
    return {
        "code": status.HTTP_200_OK,
        "data": add_order,
        "message": "success",
    }

@router.post("/order_commodity", summary='储存订单商品信息')
async def post_order_commodity(orderData:addOrderCommodity, token:str = Depends(oauth2_scheme), db:AsyncSession = Depends(db_session)):
       
    """储存订单商品详情"""
    # 这里orderData传入的是orderData的模型，所以后续需要读取属性后与数据库逻辑比较
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    add_order_commodity = OrderCommodity(
        order_id = orderData.order_id,
        u_id  = orderData.u_id,
        commodity_id  = orderData.commodity_id,
        title  = orderData.title,
        price = orderData.price,
        brand_id  = orderData.brand_id,
        category_id  = orderData.category_id,
        pictures = orderData.pictures,  
        quantity =orderData.quantity,
        create_time = datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),
        update_time = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    )
    db.add(add_order_commodity)
    await db.commit()
    await db.refresh(add_order_commodity)
    return {
        "code": status.HTTP_200_OK,
        "data": add_order_commodity,
        "message": "success",
    }

# 改用put方式
@router.put("/orderDelete", summary='删除订单信息')
async def delete_order(order_id:str,token:str = Depends(oauth2_scheme), db:AsyncSession = Depends(db_session)):
    """删除指定订单"""

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    #下面的操作会真实地删除数据库中的数据（我们要做的是添加删除时间，不进行真正的删除）

    query_sql: str = (
        update(OrderCommodity)
        .where(OrderCommodity.delete_time == None,
                OrderCommodity.order_id == order_id)
        .values(delete_time = datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
    )
    # print(query_sql)  
    result_data: ChunkedIteratorResult = await db.execute(query_sql)    
    # result_data = db.query(OrderCommodity).filter_by(OrderCommodity.order_id == order_id ).update({"delete_time":datetime.now().strftime('%Y-%m-%d  %H:%M:%S')})
    await db.commit()
    return{
        "code": status.HTTP_200_OK,
        "data": result_data,
        "message":"success"
    }
