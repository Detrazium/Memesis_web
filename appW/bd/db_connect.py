import psycopg2
# from sqlalchemy import create_async_engine
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, create_engine
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from appW.bd.schemas import met, Base

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

class create_db_tables():
	def __init__(self):
		self.creators()
	def creators(self):
		request = "postgresql+psycopg2://postgres:1111@localhost/memes_data"
		self.engine = create_engine(request)
		self.create_table()
		try:
			print('[connection is successful]')
		except:
			conn = psycopg2.connect(user='postgres', password='1111', )
			conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
			cur = conn.cursor()
			cur.execute('create database Memes_data')
			conn.close()
			self.creators()
	def create_table(self):
		Base.metadata.create_all(self.engine)

def main():
	create_db_tables()
	db_conn()

if __name__ == '__main__':
	main()
