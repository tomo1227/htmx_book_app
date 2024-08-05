import secrets

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/section3", response_class=HTMLResponse)
async def read_section3(request: Request):
    return templates.TemplateResponse("section3.html", {"request": request})


@app.get("/section4", response_class=HTMLResponse)
async def read_section4(request: Request):
    return templates.TemplateResponse("section4.html", {"request": request})


@app.get("/section5", response_class=HTMLResponse)
async def read_section5(request: Request):
    return templates.TemplateResponse("section5.html", {"request": request})


@app.get("/section6", response_class=HTMLResponse)
async def read_section6(request: Request):
    return templates.TemplateResponse("section6.html", {"request": request})


@app.get("/health_check", response_class=JSONResponse)
async def health_check():
    return {"status": "ok"}


@app.api_route("/hello", methods=["GET", "POST", "PUT", "PATCH", "DELETE"], response_class=HTMLResponse)
async def hello(request: Request):
    if request.method == "GET":
        return HTMLResponse("<span style='color:#ff0000; font-weight: bold;'>GETリクエスト!</span>")
    elif request.method == "POST":
        return HTMLResponse("<span style='color:#00ff00; font-weight: bold;'>POSTリクエスト!</span>")
    elif request.method == "PUT":
        return HTMLResponse("<span style='color:#0000ff; font-weight: bold;'>PUTリクエスト!</span>")
    elif request.method == "PATCH":
        return HTMLResponse("<span style='color:#ff00ff; font-weight: bold;'>PATCHリクエスト!</span>")
    elif request.method == "DELETE":
        return HTMLResponse("<span style='color:#ff9900; font-weight: bold;'>DELETEリクエスト!</span>")


@app.get("/random", response_class=HTMLResponse)
async def generate_random_number(request: Request):
    random_number = secrets.randbelow(10)
    html_content = f"<span style='color:#ff0000; font-weight: bold;'>{random_number}</span>"
    return HTMLResponse(html_content)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
