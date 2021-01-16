class Strategy:
    def __init__(self, name, ticker, api_key, api_secret, max_lot):
        self.name = name
        self.ticker = ticker
        self.api_key = api_key
        self.api_secret = api_secret
        self.max_lot = max_lot

    def description(self):
        return "STRATEGY(name=%s,ticker=%s,max_lot=%s)" % (self.name, self.ticker, self.max_lot)
