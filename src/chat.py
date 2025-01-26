import dataclasses
import hashlib
import json
from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/chat")
clients: List[WebSocket] = []


@dataclasses.dataclass
class Message:
    user: str
    message: str


def generate_user_id(ip_address: str) -> str:
    hashed_ip = hashlib.sha256(ip_address.encode()).hexdigest()
    return f"ID:{hashed_ip[:8]}"


@app.get("/")
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/chatroom")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    client = websocket.client
    client_ip = client[0] if client else ""
    user_id = generate_user_id(client_ip)
    clients.append(websocket)
    try:
        while True:
            raw_data = await websocket.receive_text()
            data = json.loads(raw_data)
            input_msg = data.get("message")
            now_jst = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%H:%M:%S")

            msg = f"<div hx-swap-oob='beforeend:#messages'><span>{now_jst} {user_id} > {input_msg}</span><br/></div>"

            message = Message(user=user_id, message=msg)
            await broadcast_message(message)
    except WebSocketDisconnect:
        clients.remove(websocket)


async def broadcast_message(message: Message):
    for client in clients:
        try:
            await client.send_text(json.dumps({"user": message.user, "message": message.message}))
        except Exception as e:
            print(f"Error sending message: {e}")
            await client.close()
            clients.remove(client)


app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
