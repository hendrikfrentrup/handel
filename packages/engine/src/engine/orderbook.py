from enum import Enum

class OrderType(Enum):
    BID = "Bid"
    ASK = "Ask"

class Order:
    def __init__(self, order_type: OrderType, quantity: float):
        self.order_type = order_type
        self.quantity = quantity
    
    @property
    def is_filled(self):
        return self.quantity == 0.0
    
    def __str__(self):
        return f"{self.order_type.value} for {self.quantity}"

    def __repr__(self):
        return str(self)
    

class Limit:

    def __init__(self, price: float):
        self.price = price
        self.orders = []

    def __str__(self):
        return f"{self.total_volume}@${self.price}[{len(self.orders)}]"

    def __repr__(self):
        return str(self)
    
    def add_order(self, order: Order):
        self.orders.append(order)

    @property
    def total_volume(self):
        return sum([order.quantity for order in self.orders])
    
    # TODO: implement this
    def fill_order(self, market_order: Order):
        pass

    # def volume at price(self, price: float):

class OrderBook:
    def __init__(self):
        self.bids = {}
        self.asks = {}
    
    def __str__(self):
        return f"bids: {len(self.bids)}, asks: {len(self.asks)}"

    def __repr__(self):
        return str(self)
    
    def add_limit_order(self, price: float, order: Order):
        
        match order.order_type:
            case OrderType.BID:
                # if price level does not exist in bids
                if price not in self.bids:
                    # create a new limit at price level
                    limit = Limit(price)
                    # this is interesting: add order to limit 
                    # first or limit to orderbook?
                    limit.add_order(order)
                    self.bids[price] = limit
                else:
                    self.bids[price].add_order(order)

            case OrderType.ASK:
                if price not in self.asks:
                    limit = Limit(price)
                    limit.add_order(order)
                    self.bids[price] = limit
                else:
                    limit = self.asks.get(price)
                    limit.add_order(order)
            case _:
                raise ValueError("Invalid order type")
    
    # TODO: implement this
    def fill_market_order(self, market_order: Order):
        pass