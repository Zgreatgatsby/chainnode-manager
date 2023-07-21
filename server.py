import os

from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

STATIC_FILE_PREFIX = 'static'

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.mount('/static', StaticFiles(directory=STATIC_FILE_PREFIX), name='static')


@app.get('/download/stream/{filename}')
def download_stream(filename: str):
    filepath = os.path.join(STATIC_FILE_PREFIX, filename)
    response = StreamingResponse(open(filepath, 'rb'))
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response


@app.get('/download/nornal/{filename}')
def download_normal(filename: str):
    filepath = os.path.join(STATIC_FILE_PREFIX, filename)
    response = FileResponse(open(filepath, 'rb'))
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response
