import secrets
import time

from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/tutorial")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")


def section_handler(sec):
    async def handler(request: Request):
        return templates.TemplateResponse(request, f"section{sec}.html")

    return handler


for section in range(3, 17):
    app.add_api_route(f"/section{section}", section_handler(section), response_class=HTMLResponse)


@app.get("/health_check", response_class=JSONResponse)
async def health_check():
    return {"status": "ok"}


@app.api_route("/hello", methods=["GET", "POST", "PUT", "PATCH", "DELETE"], response_class=HTMLResponse)
async def hello(request: Request):
    if request.method == "GET":
        return HTMLResponse("<span style='color:#ff0000;'>GETリクエスト!</span>")
    elif request.method == "POST":
        return HTMLResponse("<span style='color:#00bf00;'>POSTリクエスト!</span>")
    elif request.method == "PUT":
        return HTMLResponse("<span style='color:#0000ff;'>PUTリクエスト!</span>")
    elif request.method == "PATCH":
        return HTMLResponse("<span style='color:#ff00ff;'>PATCHリクエスト!</span>")
    elif request.method == "DELETE":
        return HTMLResponse("<span style='color:#ff9900;'>DELETEリクエスト!</span>")


@app.get("/random", response_class=HTMLResponse)
async def generate_random_number(request: Request):
    random_number = secrets.randbelow(10)
    html_content = f"<span style='color:#ff0000;'>{random_number}</span>"
    return HTMLResponse(html_content)


@app.get("/random_polling", response_class=HTMLResponse)
async def load_polling(request: Request):
    random_number = secrets.randbelow(10)
    html_content = f"""<p style='color:#ff0000;' hx-get='/random_polling'
                            hx-trigger='load delay:1s'>{random_number}</p>"""
    return HTMLResponse(html_content)


@app.get("/heavy", response_class=HTMLResponse)
async def heavy_load(request: Request):
    time.sleep(5)
    html_content = f"<span style='color:#ff0000;'>{'ロード完了！'}</span>"
    return HTMLResponse(html_content)


@app.post("/send-form", response_class=HTMLResponse)
async def send_form(request: Request):
    time.sleep(1)
    html_content = "<span style='color:#ff0000; font-weight: bold;'>送信完了しました。</span>"
    return HTMLResponse(html_content)


@app.post("/validate", response_class=HTMLResponse)
async def validate(request: Request):
    time.sleep(1)
    html_content = "<span style='color:#ff0000; font-weight: bold;'>正しい値を入力してください</span>"
    return HTMLResponse(html_content)


@app.post("/greeting")
async def greeting(name: str = Form(), title: str = Form()):
    html_content = f"<span style='color:#ff0000; font-weight: bold;'>{title} {name}!</span>"
    return HTMLResponse(html_content)


@app.post("/last-key")
async def display_last_key(lastkey: str = Form()):
    html_content = f"<span style='color:#ff0000; font-weight: bold;'>最後に押したキーは「{lastkey}」です。</span>"
    return HTMLResponse(html_content)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
