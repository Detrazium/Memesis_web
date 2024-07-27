from typing import AsyncGenerator
from minio import Minio as Sync_minio
from sqlalchemy.ext.asyncio import AsyncSession

from appW.bd.db_MinIO import create_bucket
from appW.bd.db_connect import db_conn, create_db_tables
from appW.bd.schemas import Memes_model, met, Table_MODEL

create_db_tables()
dbI = db_conn()
connI = dbI.engine
Declar_Memes = Table_MODEL
sessionI = dbI.Session_db

async def get_session() -> AsyncGenerator[AsyncSession, None]:
	async with sessionI() as session:
		yield session
create_bucket()
