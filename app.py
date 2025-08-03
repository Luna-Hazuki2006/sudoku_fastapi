from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from generacion import generar_matriz

app = FastAPI()

app.mount('/static', StaticFiles(directory='./static'), name='static')

templates = Jinja2Templates(directory='./templates')

@app.get('/', response_class=HTMLResponse)
def mostrar(request : Request): 
    matriz = generar_matriz()
    return templates.TemplateResponse(request, 'index.html', context={'matriz': matriz})