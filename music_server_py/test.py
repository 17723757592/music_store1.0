from typing import Union
from typing_extensions import Annotated
from fastapi import FastAPI,Body ,Form
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class UserBase(BaseModel):
    username: str
    # 请记住，传递的那些额外参数不会添加任何验证，只会添加注释，用于文档的目的。
    email: EmailStr
    full_name: Union[str, None] = None

class UserIn(UserBase):
    # 输入模型
    password: str = Form()

class UserOut(UserBase):
    # 输出
    pass

class UserInDB(UserBase):
    hashed_password: str

# user = {
#     "user1":{"username":"小强","email":"123@163.com","password":"123456","full_name":"dsdsfsf"}
# }

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    print(user_in_db)
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(
    user_in: Annotated[
        UserIn,
        Body(
            embed=True,
            examples=[{
                "username":"小强",
                "email":"123@163.com",
                "password":"123456",
                "full_name":"dsdsfsf"
            }])]):
    user_saved = fake_save_user(user_in)
    return user_saved

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)