import nest_asyncio
from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

from appW.bd.db_MinIO import GetFile

nest_asyncio.apply()

router = APIRouter(
	prefix='/icons',
	tags=['icon']
)
@router.get('/update.ico', include_in_schema=False)
async def favicon():
	return FileResponse('appW/icon/update.ico')
@router.get('/select.ico', include_in_schema=False)
async def favicon2():
	return FileResponse('appW/icon/select.ico')
@router.get('/delete.ico', include_in_schema=False)
async def favicon3():
	return FileResponse('appW/icon/delete.ico')
@router.get('/return.ico', include_in_schema=False)
async def favicon4():
	return FileResponse('appW/icon/return_ico.ico')

rute_img = APIRouter(
	prefix='/imGG',
	tags=['image']
)
@rute_img.get('/{img}', include_in_schema=False)
async def imager_get(img: str):
	await GetFile(img)
	old = f'appW/images_static/{img}'
	return FileResponse(old)