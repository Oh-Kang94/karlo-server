from fastapi import APIRouter, Response
from aiofiles import open as auifiles_open


router = APIRouter()


@router.get("/")
async def get_appcast_xml():
    async with auifiles_open('./app/static/appcast/appcast.xml', mode='r') as f:
        data = await f.read()
    return Response(content=data, media_type="application/xml")
