from aiohttp import web
import argparse

from settings import config
from handlers import health_handler, trading_view_hook_handler


def run(addr, port):
    app = web.Application()
    app.add_routes([
        web.post('/trading-view-hook-69f64a19-4108-4cb2-900a-43af0c0a440c', trading_view_hook_handler),
        web.get('/health', health_handler)
    ])
    app['config'] = config
    web.run_app(app, host=addr, port=port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8080,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
