from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

tasks = []


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("todo/index.html", {"request": request, "tasks": tasks})


@app.post("/add", response_class=HTMLResponse)
async def add_task(request: Request, task: str = Form(...)):
    tasks.append(task)
    return templates.TemplateResponse("todo/task.html", {"request": request, "task": task})


@app.delete("/delete", response_class=HTMLResponse)
async def delete_task(task: str):
    if task in tasks:
        tasks.remove(task)
    return HTMLResponse(content="", status_code=204)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
