from sqlalchemy import Integer, String, Text, Column, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

met = MetaData()
Memes_model = Table(
	'Mem_info', met,
Column('id', Integer,autoincrement=True, primary_key=True, ),
	 Column('name', String, nullable=False),
	 Column('des_', Text, nullable=False),
	 Column('Img_id', Text)
					)