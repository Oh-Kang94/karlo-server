import base64
import os
import uuid
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.services.karlo_service import KarloService
from app.services.translate_service import TranslateService


class Item(BaseModel):
    keyword: str


class Base64Request(BaseModel):
    base64_file: str


class Base64Response(BaseModel):
    response_code: str
    response_message: str


router = APIRouter()


@router.post("/")
async def get_images(item: Item):
    query: str = item.keyword
    print(query)
    # query = TranslateService.translate_text_to_en(query)
    images = KarloService.get_text_to_images_url(query)
    return JSONResponse(content={"result": images})

#  Upload Base64 Image


@router.post("/photo")
async def upload_photo(base64_image: Base64Request):
    UPLOAD_DIR = "./app/photo"  # 이미지를 저장할 서버 경로
    imgStr = base64_image.base64_file
    imgData = base64.b64decode(imgStr)
    filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
    with open(os.path.join(UPLOAD_DIR, filename), "wb") as f:
        f.write(imgData)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)
    return {"filename": filename}

# Upload Raw Image
# @router.post("/photo")
# async def upload_photo(file: UploadFile):
#     UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로

#     content = await file.read()
#     filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
#     with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
#         fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)

#     return {"filename": filename}
