from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health_check", response_class=JSONResponse)
async def health_check():
    return {"status": "ok"}

@app.api_route("/hello", methods=["GET", "POST", "PUT", "PATCH", "DELETE"], response_class=HTMLResponse)
async def handle_request(request: Request):
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

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/section1", response_class=HTMLResponse)
async def read_section1(request: Request):
    return templates.TemplateResponse("section1.html", {"request": request})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
