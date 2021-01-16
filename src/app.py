import logging

from decimal import *
from binance_f.model.constant import *

import binance
import config
from order import Order
import telegram


def process_message(message: dict):
    logging.info("got message: [%s]", message)
    order = parse_order(message)
    validate(order)
    order_info = order.description()
    logging.info(order_info)
    try:
        binance.place_order(order)
        telegram.post_message(order_info)
    except Exception as e:
        error = "%s %s %s" % (type(e), e.args, e)
        logging.error(error)
        telegram.post_message("=" * 80 + "\nERROR: " + order_info + "; " + error)


def parse_order(message: dict):
    ticker = get_ticker(message)
    side = parse_trading_side(message)
    size = parse_trading_size(message)
    strategy = get_strategy(message)
    return Order(ticker, side, size, strategy)


def validate(o: Order):
    if o.ticker != o.strategy.ticker:
        raise ValueError("strategy [%s] does not match to ticker [%s]" % (o.strategy.name, o.ticker))
    if o.size > o.strategy.max_lot:
        raise ValueError("strategy [%s] max lot size exceeded [%s > %s]" % (o.strategy.name, o.size, o.strategy.max_lot))


def get_ticker(message: dict):
    ticker = message.get("ticker")  # "XRPUSDTPERP"
    if not ticker:
        raise KeyError("message body has no \"ticker\"")
    transformed = config.TICKER_MAPPING.get(ticker)
    if not transformed:
        raise KeyError("unknown ticker [%s]" % ticker)
    return transformed


def parse_trading_side(message: dict):
    action = message.get("order.action")  # "sell"
    if not action:
        raise KeyError("message body has no \"order.action\"")
    side = {'buy': OrderSide.BUY, 'sell': OrderSide.SELL}.get(action)
    if not side:
        raise KeyError("unknown action [%s]" % action)
    return side


def parse_trading_size(message: dict):
    size = message["order.contracts"]  # "0.2"
    if not size:
        raise KeyError("message body has no \"size\"")
    try:
        return Decimal(size)
    except InvalidOperation:
        raise ValueError("wrong size value [%s]" % size)


def get_strategy(message: dict):
    strategy_name = message["strategy_name"]  # "strategy-001"
    if not strategy_name:
        raise KeyError("message body has no \"strategy_name\"")
    strategy = config.STRATEGY_TICKER_MAPPING.get(strategy_name)
    if not strategy:
        raise KeyError("unknown strategy [%s]" % strategy_name)
    return strategy
