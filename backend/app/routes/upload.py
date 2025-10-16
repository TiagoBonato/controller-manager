from fastapi import APIRouter, UploadFile
import json

router = APIRouter()

@router.post("/upload")
async def upload_config(file: UploadFile):
    content = await file.read()
    data = json.loads(content)
    return {"status": "success", "data": data}