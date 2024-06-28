from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health_check", response_class=JSONResponse)
async def health_check():
    return {"status": "ok"}


@app.get("/hello", response_class=HTMLResponse)
async def hello(request: Request):
    return HTMLResponse("<p>Hello HTMX!</p>")

