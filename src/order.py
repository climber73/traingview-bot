class Order:
    def __init__(self, ticker, side, size, strategy):
        self.ticker = ticker
        self.side = side
        self.size = size
        self.strategy = strategy

    def description(self):
        return "ORDER(ticker=%s,side=%s,size=%s,strategy=%s)" % \
               (self.ticker, self.side, self.size, self.strategy.description())
