# app/main.py
import os
from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_200_OK

from core import resume_data as r
from core import projects as p

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

os.makedirs("logs", exist_ok=True)

@app.get('/')
async def home(request: Request) -> HTMLResponse:
    _context = dict()
    _context['name'] = r.contact_info['name']
    _context['address'] = r.contact_info['address']
    _context['phone'] = r.contact_info['phone']
    _context['email'] = r.contact_info['email']
    _context['github'] = r.contact_info['github']
    _context['professional_summary'] = r.professional_summary
    _context['certifications'] = r.certifications
    _context['education'] = r.education
    _context['bullets'] = r.bullets
    _context['jobs'] = r.jobs
    return templates.TemplateResponse(
        request=request,
        context=_context,
        name="home.html",
        status_code=status.HTTP_200_OK
    )

@app.get('/projects')
async def project_index(request: Request) -> HTMLResponse:
    _context = dict()
    _context = p.projects
    return templates.TemplateResponse(
        request=request,
        context=_context,
        name="projects/project_index.html",
        status_code=status.HTTP_200_OK
    )

@app.get('/projects/little_rock')
async def project_little_rock(request: Request) -> HTMLResponse:
    _context = dict()
    _context = p.projects
    return templates.TemplateResponse(
        request=request,
        context=_context,
        name="projects/project_index.html",
        status_code=status.HTTP_200_OK
    )