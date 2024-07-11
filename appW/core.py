import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from appW.routers import router as router_operator

app =  FastAPI(title='PAGE_NAEM_FRONT')
app.mount('/appW/static', StaticFiles(directory='appW/static'), name='static')
app.include_router(router_operator)

