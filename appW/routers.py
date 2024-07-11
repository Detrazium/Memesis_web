from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from appW import templates
from pydantic import BaseModel

router = APIRouter(
	prefix='/Operatro',
	tags=['operation']
)

class baser(BaseModel):
	id: int
	name: str
	currenter: str
	DATOID: str
	base_id: int

@router.get('/memes', response_class=HTMLResponse)
async def get_all_memes(request: Request):
	return templates.TemplateResponse(name='all_memes.html', context={'request': request})

@router.get('/memes/{id}', response_class=HTMLResponse)
async def get_id_memes(request: Request):
	return templates.TemplateResponse(name='all_memes.html', context={'request': request})

@router.post('/memes', response_class=HTMLResponse)
async def new_mem(request: Request):
	return templates.TemplateResponse(name='all_memes.html', context={'request': request})

@router.put('/memes/{id}', response_class=HTMLResponse)
async def update_mem(request: Request):
	return templates.TemplateResponse(name='all_memes.html', context={'request': request})

@router.delete('/memes/{id}', response_class=HTMLResponse)
async def delete_mem(request: Request):
	return templates.TemplateResponse(name='all_memes.html', context={'request': request})