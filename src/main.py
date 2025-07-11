## -*- coding: utf-8 -*-
import secrets
import time
from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/tutorial")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
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


@app.get("/yahoo", response_class=HTMLResponse)
async def yahoo(request: Request):
    return HTMLResponse("<span style='color:#ff0000;'>やっほー!</span>")


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


@app.get("/success")
async def get_success(request: Request):
    html_content = "<span style='color:#ff0000; font-weight: bold;'>Success!</span>"
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/not-found")
async def get_not_found(request: Request):
    html_content = "<span style='color:#ff0000; font-weight: bold;'>Not Found!</span>"
    return HTMLResponse(content=html_content, status_code=404)


@app.get("/server-error")
async def get_server_error(request: Request):
    html_content = "<span style='color:#ff0000; font-weight: bold;'>Internal Server Error!</span>"
    return HTMLResponse(content=html_content, status_code=500)


colors = ["blue", "green", "orange", "red"]


@app.get("/colors", response_class=HTMLResponse)
def get_colors():
    color = colors.pop(0)
    colors.append(color)
    return f"""<div hx-get="/colors" hx-swap="outerHTML" class="smooth" hx-trigger="every 1s" style="color:{color}">
                こんにちは！
            </div>"""


@app.get("/en-saying", response_class=HTMLResponse)
async def en_saying():
    return """
    <p>Embrace challenges, for they are the stepping stones to growth.</p>
    <button hx-get='/ja-saying' hx-swap='innerHTML transition:true' hx-target='closest div'>
        翻訳する
    </button>
    """


@app.get("/ja-saying", response_class=HTMLResponse)
async def ja_saying():
    return """
    <p>挑戦を受け入れよう。それらは成長への踏み石なのだから。</p>
    <button hx-get='/en-saying' hx-swap='innerHTML transition:true' hx-target='closest div'>
        原文に戻す
    </button>
    """


@app.get("/update-title", response_class=HTMLResponse)
async def update_title():
    return """
    <title>New Title</title>
    <p>hello!</p>
    """


@app.get("/update-head", response_class=HTMLResponse)
async def update_head():
    return """
    <head hx-head="merge">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI with htmx</title>
        <link rel="stylesheet" href="/static/styles/tutorial2.css">
    </head>
    """


@app.get("/re-eval-head", response_class=HTMLResponse)
async def re_eval_head():
    return """
    <head hx-head="re-eval">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI with htmx</title>
        <link rel="stylesheet" href="/static/styles/tutorial2.css">
    </head>
    """


@app.get("/append-head", response_class=HTMLResponse)
async def add_head_style():
    return """
    <head hx-head="append">
        <link rel="stylesheet" href="/static/styles/tutorial2.css">
    </head>
    """


@app.post("/now", response_class=HTMLResponse)
async def get_now():
    now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%H:%M:%S")
    time.sleep(2)

    return f"<div>{now}</div>"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
