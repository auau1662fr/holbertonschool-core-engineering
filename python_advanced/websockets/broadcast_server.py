#!/usr/bin/env python3
"""WebSocket server with broadcast messaging"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Handle incoming WebSocket connections with broadcast messaging"""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in set(connected_clients):
                await client.send(f"B:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket broadcast server"""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
