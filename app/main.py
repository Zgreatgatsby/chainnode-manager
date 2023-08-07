import os

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routers import staticfile
from app.internal.config import STATIC_FILE_DIR, ROOT_DIR

static_file_dir = os.path.join(ROOT_DIR, STATIC_FILE_DIR)
if not os.path.exists(static_file_dir):
    os.mkdir(static_file_dir)

app = FastAPI(dependencies=[])
# app.add_middleware(GZipMiddleware, minimum_size=1000)
app.mount('/static', StaticFiles(directory=static_file_dir), name='static')
app.include_router(staticfile.router)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/ping")
async def ping():
    return "pong"


@app.get("/static", response_class=HTMLResponse)
def list_files(request: Request):

    files = os.listdir(static_file_dir)
    files_paths = sorted([{"path": f, "url": f"{request.url._url}/{f}"} for f in files], key=lambda x: x["path"])
    return templates.TemplateResponse(
        "list_files.html", {"request": request, "files": files_paths}
    )
