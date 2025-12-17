# app/main.py
import os

from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

os.makedirs("logs", exist_ok=True)

@app.get('/')
async def home(
        request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="base.html",
        status_code=status.HTTP_200_OK
    )