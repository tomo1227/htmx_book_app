from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/health_check", response_class=JSONResponse)
async def health_check():
    return {"status": "ok"}


@app.get("/load_content", response_class=HTMLResponse)
async def load_content(request: Request):
    return HTMLResponse("<p>新しいコンテンツがロードされました！</p>")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
