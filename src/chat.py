import dataclasses
import hashlib
import json
from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/chat")
clients: List[WebSocket] = []


@dataclasses.dataclass
class Message:
    userid: str
    username: str
    message: str


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request, "index.html")


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
            input_name = data.get("name")
            input_msg = data.get("message")
            now_jst = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%H:%M:%S")
            msg = f"""
                            <div hx-swap-oob='beforeend:#messages'>
                                <span>
                                    <span style='color:green'>{input_name}</span>
                                    <span style='color:blue'>{now_jst}</span>
                                    <span style='color:purple'>{user_id}</span>
                                    <span>{input_msg}</span>
                                </span>
                            </div>
                        """
            message = Message(userid=user_id, username=input_name, message=msg.replace("\n", ""))
            await broadcast_message(message)
    except WebSocketDisconnect:
        clients.remove(websocket)


async def broadcast_message(message: Message):
    for client in clients:
        try:
            await client.send_text(
                json.dumps(
                    {"username": message.username, "userid": message.userid, "message": message.message},
                    ensure_ascii=False,
                )
            )
        except Exception as e:
            print(f"Error sending message: {e}")
            await client.close()
            clients.remove(client)


def generate_user_id(ip_address: str) -> str:
    hashed_ip = hashlib.sha256(ip_address.encode()).hexdigest()
    return f"ID:{hashed_ip[:8]}"


# コンテナの場合は以下を記述
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
