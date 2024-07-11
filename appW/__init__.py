from starlette.templating import Jinja2Templates

from appW.bd.database import bd

bd = None
templates = Jinja2Templates(directory='appW/templates')