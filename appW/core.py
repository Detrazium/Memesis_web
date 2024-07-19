import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from appW.routers import router as router_operator

app =  FastAPI(title='PAGE_NAEM_FRONT')
app.mount('/appW/static', StaticFiles(directory='appW/static'), name='static')
app.mount('/appW/images_static', StaticFiles(directory='appW/images_static'), name='images_static')
app.mount('/app/icon', StaticFiles(directory='appW/icon'), name='icon')
from appW.rout_icons import router as icon_rout
app.include_router(icon_rout)
app.include_router(router_operator)

