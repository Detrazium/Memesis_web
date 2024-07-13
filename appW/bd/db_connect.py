import psycopg2
# from sqlalchemy import create_async_engine
from sqlalchemy import MetaData, Table, String, Integer, Column, Text
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.ddl import CreateTable


class db_conn:
	def __init__(self):
		self.create_enginers()
	def create_enginers(self):
		request = "postgresql+asyncpg://postgres:1111@localhost/memes_data"
		self.engine = create_async_engine(request)
		self.engine.connect()
		self.get_session()
		try:
			print('[connection is successful]')
		except:
			conn = psycopg2.connect(user='postgres', password='1111', )
			conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
			cur = conn.cursor()
			cur.execute('create database Memes_data')
			conn.close()
			self.create_enginers()
	def get_session(self):
		self.Session_db = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

# async with db_conn.Session_db as session:
# 	met = MetaData()
# 	mem_info = Table('Mem_info', met,
# 					 Column('id', Integer(), primary_key=True, ),
# 					 Column('name', String(400), nullable=False),
# 					 Column('des_', Text(), nullable=False),
# 					 Column('Img_id', Text()))
# 	create_expp = CreateTable(mem_info)
# 	await session.execute(create_expp)

def main():
	db_conn()

if __name__ == '__main__':
	main()
