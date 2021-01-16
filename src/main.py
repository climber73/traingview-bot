from aiohttp import web

from settings import config
from handlers import health_handler, trading_view_hook_handler

app = web.Application()
app.add_routes([
    web.post('/trading-view-hook-69f64a19-4108-4cb2-900a-43af0c0a440c', trading_view_hook_handler),
    web.get('/health', health_handler)
])
app['config'] = config
web.run_app(app)
