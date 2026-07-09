#!/usr/bin/env python3
"""ASGI WebSocket server using Starlette"""
from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.staticfiles import StaticFiles


async def homepage(request):
    """Serve the homepage"""
    return FileResponse("index.html")


async def websocket_endpoint(websocket):
    """Handle WebSocket connections with echo behavior"""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except Exception:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])

app.mount("/", StaticFiles(directory="."), name="static")
