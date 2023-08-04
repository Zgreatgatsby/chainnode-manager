import os

from fastapi import Depends, FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import staticfile
from app.internal.config import STATIC_FILE_DIR, ROOT_DIR

static_file_dir = os.path.join(ROOT_DIR, STATIC_FILE_DIR)
if not os.path.exists(static_file_dir):
    os.mkdir(static_file_dir)

app = FastAPI(dependencies=[])
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.mount('/static', StaticFiles(directory=static_file_dir), name='static')
app.include_router(staticfile.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/ping")
async def ping():
    return "pong"
