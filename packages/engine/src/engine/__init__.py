def hello() -> str:
    return "Hello from handel!"

# doc: symbol of the security being traded
class Symbol:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return str(self)
    

class Engine:

    # doc: initialise as an empty collection of orderbooks
    def __init__(self):
        self.orderbooks = {}

    def __str__(self):
        return f"Engine for {len(self.orderbooks.items())}"

    def __repr__(self):
        return str(self)
    
    def create_new_market(self, symbol: Symbol):
        self.orderbooks[symbol] = [] # OrderBook