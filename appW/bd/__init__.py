from msilib import Table
from typing import AsyncGenerator

from sqlalchemy import MetaData, Column, Integer, String, Text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.ddl import CreateTable

from appW.bd.db_connect import db_conn
from appW.bd.schemas import Memes_model

dbI = db_conn()
connI = dbI.engine

sessionI = dbI.Session_db
Table_memesI = Memes_model

async def get_session() -> AsyncGenerator[AsyncSession, None]:
	async with sessionI() as session:
		yield session