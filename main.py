import uvicorn

if __name__ =='__main__':
	uvicorn.run('appW.core:app', host='localhost', port=8000, reload=True)
