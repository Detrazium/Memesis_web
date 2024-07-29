import uvicorn
"""Локальный запуск из проекта напрямую"""
if __name__ =='__main__':
	uvicorn.run('appW.core:app', host='0.0.0.0', port=8020, reload=True)