from starlette.templating import Jinja2Templates

from appW.bd.methods import method

bd = method()
templates = Jinja2Templates(directory='appW/templates')