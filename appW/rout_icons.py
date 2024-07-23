from fastapi import APIRouter
from fastapi.responses import FileResponse

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
	return FileResponse(f'appW/images_static/{img}')