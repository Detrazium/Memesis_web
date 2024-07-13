from appW.bd import sessionI, Table_memesI

class method():
	def __init__(self):
		bd = None
	async def get_all(self):
		All_memes = sessionI.query(Table_memesI).all()
		return All_memes
	async def get_id(self, id:int):
		mem = sessionI.get(Table_memesI, id)
		return mem
	async def create_mem(self, name:str, des_:str, img:str = None):
		Memes = Table_memesI(name, des_, img)
		sessionI.add(Memes)
		l = Memes.name
		sessionI.commit()
		print(l, ' create_complete')
	async def update(self, id:int, name:str, des_:str, img:str = None):
		Mem = sessionI.query(Table_memesI).filter(Table_memesI.id == id).first()
		Mem.name = name
		Mem.des_ = des_
		Mem.img = img
		sessionI.commit()
		print('/update_complete/')
	async def delete(self, id:int):
		mem = sessionI.query(Table_memesI).filter(Table_memesI.id == id).first()
		sessionI.delete(mem)
		sessionI.commit()
		print('/delete_complete/')

