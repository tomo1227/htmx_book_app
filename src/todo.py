from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/todo")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/add", response_class=HTMLResponse)
async def add_task(request: Request, task: str = Form(...)):
    return templates.TemplateResponse(request, "task.html", {"task": task})


@app.delete("/delete", response_class=HTMLResponse)
async def delete_task(task: str):
    return HTMLResponse(content="", status_code=204)


# コンテナの場合は以下を記述
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
