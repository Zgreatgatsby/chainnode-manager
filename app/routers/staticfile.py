import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

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
