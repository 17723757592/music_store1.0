from fastapi import FastAPI
import asyncio
import nest_asyncio
from fastapi.middleware.cors import CORSMiddleware
from app.exceptions import register_exception_handler
from app.routers import commodity, banner, user
# nest_asyncio.apply()

app = FastAPI(title="音乐商城", description="音乐商场", version="0.0.1")

origins = [
    "http://localhost",
    "http://localhost:8080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# hander = register_exception_handler(app=app)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hander)

# asyncio.run(hander)
hander = register_exception_handler(app=app)
task = asyncio.create_task(hander)
app.include_router(commodity.router, prefix="/commodity", tags=["商品"])
app.include_router(banner.router, prefix="/banner", tags=["Banner"])
app.include_router(user.router, prefix="/user", tags=["User"])
