from fastapi import APIRouter,Request
from typing import Union
from fastapi import Depends
from mysql.connector import cursor
from db import get_db
from starlette.templating import Jinja2Templates

root_router = APIRouter()
templates = Jinja2Templates(directory="static")


@root_router.get("/demo")
async def root():
    return templates.TemplateResponse("demo.html")

@root_router.get("/")
async def find_user(
        request:Request,
        user_id: Union[int, None] = None,
        user_name: Union[str, None] = None,
        db: cursor.MySQLCursor = Depends(get_db)
    ):
    if user_id:
        query = "SELECT * FROM student WHERE Sno = %s"
        db.execute(query, (user_id,))
        print(user_id)
    if user_name:
        query = "SELECT * FROM student WHERE Snam = %s"
        db.execute(query, (user_name,))
    result = db.fetchall()
    if result:
        print(result[0][1])
        print(request,6666)
        # return {"user_id": result[0][0], "username": result[0][1]}
        return templates.TemplateResponse("demo.html",{
            "request":request,
            # "id":result[0],
            # "name":result[1]
            "result":result
            })
    else:
        return {"error": "User not found"}
