import secrets
import time

from fastapi import FastAPI, Form, Request
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


@app.get("/section7", response_class=HTMLResponse)
async def read_section7(request: Request):
    return templates.TemplateResponse("section7.html", {"request": request})


@app.get("/section8", response_class=HTMLResponse)
async def read_section8(request: Request):
    return templates.TemplateResponse("section8.html", {"request": request})


@app.get("/section9", response_class=HTMLResponse)
async def read_section9(request: Request):
    return templates.TemplateResponse("section9.html", {"request": request})


@app.get("/section10", response_class=HTMLResponse)
async def read_section10(request: Request):
    return templates.TemplateResponse("section10.html", {"request": request})


@app.get("/section11", response_class=HTMLResponse)
async def read_section11(request: Request):
    return templates.TemplateResponse("section11.html", {"request": request})


@app.get("/section12", response_class=HTMLResponse)
async def read_section12(request: Request):
    return templates.TemplateResponse("section12.html", {"request": request})


@app.get("/section13", response_class=HTMLResponse)
async def read_section13(request: Request):
    return templates.TemplateResponse("section13.html", {"request": request})


@app.get("/section14", response_class=HTMLResponse)
async def read_section14(request: Request):
    return templates.TemplateResponse("section14.html", {"request": request})


@app.get("/section15", response_class=HTMLResponse)
async def read_section15(request: Request):
    return templates.TemplateResponse("section15.html", {"request": request})


@app.get("/section16", response_class=HTMLResponse)
async def read_section16(request: Request):
    return templates.TemplateResponse("section16.html", {"request": request})


@app.get("/section17", response_class=HTMLResponse)
async def read_section17(request: Request):
    return templates.TemplateResponse("section17.html", {"request": request})


@app.get("/section18", response_class=HTMLResponse)
async def read_section18(request: Request):
    return templates.TemplateResponse("section18.html", {"request": request})


@app.get("/section19", response_class=HTMLResponse)
async def read_section19(request: Request):
    return templates.TemplateResponse("section19.html", {"request": request})


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


@app.get("/random_polling", response_class=HTMLResponse)
async def load_polling(request: Request):
    random_number = secrets.randbelow(10)
    html_content = f"""<p style='color:#ff0000; font-weight: bold;' hx-get='/random_polling'
                            hx-trigger='load delay:1s'>{random_number}</p>"""
    return HTMLResponse(html_content)


@app.get("/heavy", response_class=HTMLResponse)
async def heavy_load(request: Request):
    time.sleep(5)
    html_content = f"<span style='color:#ff0000; font-weight: bold;'>{'ロード完了！'}</span>"
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
