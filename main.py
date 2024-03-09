from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./views")

@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return templates.TemplateResponse("login.html", {"request": req})
