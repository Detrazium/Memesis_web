import uvicorn
import atexit
from appW.bd.cleaner_image import Del_ImgStart


def exit_handler():
	print('чистка подгруженных фотографий... ')
	Del_ImgStart()

atexit.register(exit_handler)
if __name__ =='__main__':
	uvicorn.run('appW.core:app', host='localhost', port=8020, reload=True)