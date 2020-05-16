from aiohttp import web
import asyncio
import time

import pytest


async def hello(request):
    return web.Response(body=b'helth is ok')

def create_app(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/health', hello)
    return app


# @pytest.mark.asyncio
# async def test_health(test_client):
#     client = await test_client(create_app)
#     resp = await client.get('/healt')
#     assert resp.status == 200
#     text = await resp.text()
#     assert 'helth is ok' in text


# async def test_coro(event_loop):
# #     before = time.monotonic()
# #     await asyncio.sleep(0.1, loop=event_loop)
# #     after = time.monotonic()
# #     assert after - before >= 0.1