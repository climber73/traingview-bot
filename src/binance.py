import logging

from binance_f import RequestClient
from binance_f.base.printobject import *
from binance_f.model.constant import *
import config
from threading import Lock
lock = Lock()

binance_url = "https://fapi.binance.com"
clients = {}


def place_order(o):
    client = get_client(o.strategy)
    if not config.DRY_RUN:
        result = client.post_order(symbol=o.ticker, side=o.side, ordertype=OrderType.MARKET, quantity=o.size)
        PrintBasic.print_obj(result)
        logging.info("order placed: [%s]" % result.__dict__)
    else:
        logging.info("DRY_RUN: no order was placed")


def get_client(strategy):
    k = strategy.api_key + strategy.api_secret
    client = clients.get(k)
    if client:
        return client
    else:
        with lock:
            client = RequestClient(api_key=strategy.api_key, secret_key=strategy.api_secret, url=binance_url)
            clients[k] = client
            return client
