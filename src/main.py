from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Portal Corporativo")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/oportunidades-salesforce")
async def salesforce():
    return {
        "dashboard": "Oportunidades Salesforce"
    }


@app.get("/atuacoes")
async def atuacoes():
    return {
        "dashboard": "Atuações"
    }


@app.get("/farol")
async def farol():
    return {
        "dashboard": "Farol"
    }