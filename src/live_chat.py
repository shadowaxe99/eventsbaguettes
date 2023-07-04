```python
import asyncio
from aiohttp import web

class LiveChat:
    def __init__(self):
        self.users = {}

    async def register(self, websocket):
        user_id = id(websocket)
        self.users[user_id] = websocket
        return user_id

    async def unregister(self, user_id):
        websocket = self.users.pop(user_id)
        await websocket.close()

    async def send_message(self, user_id, message):
        websocket = self.users[user_id]
        await websocket.send_str(message)

    async def broadcast(self, message):
        for websocket in self.users.values():
            await websocket.send_str(message)

    async def handle_websocket(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        user_id = await self.register(ws)
        try:
            async for msg in ws:
                if msg.type == web.WSMsgType.TEXT:
                    await self.broadcast(msg.data)
        finally:
            await self.unregister(user_id)

        return ws

live_chat = LiveChat()
app = web.Application()
app.router.add_get('/ws', live_chat.handle_websocket)

if __name__ == '__main__':
    web.run_app(app)
```