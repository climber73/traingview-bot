from strategy import Strategy
from secrets import \
    STRATEGY_001_API_KEY, STRATEGY_001_API_SECRET, \
    STRATEGY_002_API_KEY, STRATEGY_002_API_SECRET

STRATEGY_TICKER_MAPPING = {
    "strategy-001": Strategy(name="strategy-001", ticker="XRPUSDT",
                             api_key=STRATEGY_001_API_KEY,
                             api_secret=STRATEGY_001_API_SECRET,
                             max_lot=4000.0),
    "strategy-002": Strategy(name="strategy-002", ticker="ETHUSDT",
                             api_key=STRATEGY_002_API_KEY,
                             api_secret=STRATEGY_002_API_SECRET,
                             max_lot=4.0),
}

TICKER_MAPPING = {
    "XRPUSDTPERP": "XRPUSDT",
    "ETHUSDTPERP": "ETHUSDT",
    "BTCUSDTPERP": "BTCUSDT",
}

DRY_RUN = False
