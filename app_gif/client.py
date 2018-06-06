import aiohttp
import asyncio
from aiohttp import WSMsgType


async def ws_client():
    session = aiohttp.ClientSession()
    async with session.ws_connect('http://0.0.0.0:8080/ws') as ws:
        await prompt(ws)
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                print('Receive fom server: %s' % msg.data)
                if msg.data == 'close':
                    ws.close()
                else:
                    await prompt(ws)
            elif msg.type == WSMsgType.ERROR:
                print('Exception')


async def prompt(ws):
    msg = input('Type message:')
    await ws.send_str(msg)

asyncio.get_event_loop().run_until_complete(ws_client())