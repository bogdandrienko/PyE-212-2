from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return "Hello World"


@app.get("/home/", response_class=HTMLResponse)
async def home(request: Request):
    name = "Alice"
    return templates.TemplateResponse("hello.html", {"request": request, "name": name})
