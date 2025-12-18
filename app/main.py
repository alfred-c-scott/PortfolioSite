# app/main.py
import os
from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from core import resume_data as r
from core.config import settings

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

os.makedirs("logs", exist_ok=True)

@app.get('/')
async def home(request: Request) -> HTMLResponse:
    _context = dict()
    _context['name'] = settings.name
    _context['address'] = settings.address
    _context['phone'] = settings.phone
    _context['email'] = settings.email
    _context['github'] = settings.github
    _context['professional_summary'] = r.professional_summary
    _context['bullets'] = r.bullets
    _context['jobs'] = r.jobs
    return templates.TemplateResponse(
        request=request,
        context=_context,
        name="home.html",
        status_code=status.HTTP_200_OK
    )

