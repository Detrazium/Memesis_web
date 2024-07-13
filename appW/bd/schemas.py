from sqlalchemy import Integer, String, Text, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase): pass
class Memes_model(Base):
	__tablename__ = 'Mem_info'
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	des_ = Column(Text)
	Img_id = Column(Text)