import os
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

from app.internal.config import STATIC_FILE_DIR, ROOT_DIR

static_file_dir = os.path.join(ROOT_DIR, STATIC_FILE_DIR)
router = APIRouter()


@router.get('/download/{filename}')
async def download_normal(filename: str):
    filepath = os.path.join(static_file_dir, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail='File not found')
    response = FileResponse(filepath)
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response


@router.get("/static/{path:path}")
async def serve_file(path: str):
    full_path = Path(static_file_dir) / path
    if full_path.is_file():
        return FileResponse(full_path)
    elif full_path.is_dir():
        return HTMLResponse(generate_directory_listing(full_path))
    else:
        raise HTTPException(status_code=404, detail="File not found")


def generate_directory_listing(directory_path):
    listing = "<h1>Directory Listing</h1>"
    listing += "<ul>"
    for item in directory_path.iterdir():
        listing += f"<li><a href='{item.name}'>{item.name}</a></li>"
    listing += "</ul>"
    return listing
