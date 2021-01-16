import aiohttp
from aiohttp import web
from aiohttp.web_exceptions import HTTPForbidden, HTTPBadRequest
import logging

import app
import secrets
import telegram

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


async def health_handler(request):
    return web.Response(text='OK')


async def trading_view_hook_handler(request):
    if not request.body_exists or not request.can_read_body:
        raise HTTPBadRequest()
    body = await request.json()
    await check_auth(request, body)
    logging.info("=" * 80)
    logging.info("got trading_view hook: [%s]" % body)
    try:
        app.process_message(body)
    except (KeyError, ValueError) as e:
        message = "%s %s %s" % (type(e), e.args, e)
        logging.error(message)
        telegram.post_message("=" * 80 + "\nERROR: " + message)
        raise HTTPBadRequest(body=message.encode('utf-8'))
    return web.Response(text='OK')


async def check_auth(request, body):
    if request.version != aiohttp.HttpVersion11:
        return
    # if request.headers.get('AUTHORIZATION') is None:
    #     raise HTTPForbidden()
    if "token" not in body or body["token"] != secrets.AUTH_TOKEN:
        raise HTTPForbidden()
    body.pop("token")  # prevent logging of sensitive info
