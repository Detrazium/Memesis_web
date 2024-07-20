from fastapi import APIRouter, Depends, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from appW.bd.methods import method
from appW import templates
from appW.bd import get_session, Table_memesI

router = APIRouter(
	prefix='/Operatro',
	tags=['operation']
)
@router.get('/memes')
async def get_all_memes(request: Request, session: AsyncSession = Depends(get_session)):
	"""Получить список мемов"""
	items = select(Table_memesI)
	all_items = await session.execute(items)
	return templates.TemplateResponse(name='all_memes.html', context={'request': request, 'db_data': all_items.all()})

@router.get('/memes/{id}')
async def get_id_memes(id: int, request: Request, session: AsyncSession = Depends(get_session)):
	"""Получить конкретный мем"""
	qwert = select(Table_memesI).where(Table_memesI.id == id)
	item = await session.execute(qwert)
	return templates.TemplateResponse(name='all_memes.html', context={'request': request, "ID_MEMES": item})

class Item(BaseModel):
	name: str
	image: str
	descr: str
@router.post('/memes')
async def new_mem(data: Item):
	"""Добавить новый мем"""
	print('Input_itog: ', data)
	return

@router.put('/memes/{id}', response_class=HTMLResponse)
async def update_mem(request: Request):
	"""Обновить существующий мем"""
	return templates.TemplateResponse(name='all_memes.html', context={'request': request})

@router.delete('/memes/{id}', response_class=HTMLResponse)
async def delete_mem(request: Request):
	"""Удалить мем"""
	return templates.TemplateResponse(name='all_memes.html', context={'request': request})