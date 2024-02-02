from fastapi import FastAPI, Depends, Query
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import cursor
from db import get_db
import json 
from starlette.staticfiles import StaticFiles
from root import root_router

app = FastAPI()

# app.include_router(docs.router,prefix="/api",tags=["hhha"])
app.include_router(root_router)

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# def get_db(db: cursor.MySQLCursor = Depends(get_db)):
#     return db

@app.get("/student")
async def get_users(db: cursor.MySQLCursor = Depends(get_db)):
    query = "SELECT * FROM student"
    db.execute(query)
    result = db.fetchall()
    if result:
        return {"student": result}
    else:
        return {"error": "Student not found"}
    
# @app.get("/student/")
# async def find_user(
#         user_id: Union[str, None] = None,
#         user_name: Union[str, None] = None,
#         db: cursor.MySQLCursor = Depends(get_db)
#     ):
#     if user_id:
#         query = "SELECT * FROM student WHERE Sno = %s"
#         db.execute(query, (user_id,))
#     if user_name:
#         query = "SELECT * FROM student WHERE Snam = %s"
#         db.execute(query, (user_name,))
#     result = db.fetchall()
#     if result:
#         # return {"user_id": result[0][0], "username": result[0][1]}
#         return(result)
#     else:
#         return {"error": "User not found"}
    
# @app.get("/student/{user_name}")
# async def find_user(user_name: str,
#                       db: cursor.MySQLCursor = Depends(get_db)):
#     query = "SELECT * FROM student WHERE Snam = %s"
#     db.execute(query, (user_name,))
#     result = db.fetchone()
#     print(result,user_name)
#     return {result}

    # query = "INSERT INTO student () VALUES (%s)"
    # db.execute(query, (user_name,))
    # result = db.fetchone()
    # db.execute("COMMIT")
    # return {result}

app.mount("/static",StaticFiles(directory="static"),name="static")
# 第一个 /static 指的是这个“子应用程序”将被“安装”到的子路径，因此，任何以 /static 开头的路径都将由它处理
#  directory="static"  是指包含静态文件的目录的名称，本地目录
#  name="static"  赋予它一个可以被 FastAPI 内部使用的名称，这里暂时没用到

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)