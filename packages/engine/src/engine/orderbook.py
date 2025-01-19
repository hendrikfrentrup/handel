
from typing import Dict

from .order import Order, OrderType
from .limit import Limit

class OrderBook:
    def __init__(self):
        self.bids: Dict[float, Limit] = {}
        self.asks: Dict[float, Limit] = {}
    
    def __str__(self):
        return f"bids: {len(self.bids)}, asks: {len(self.asks)}"

    def __repr__(self):
        return str(self)
    
    def _add_order_or_create_limit(self, price: float, order: Order, orders: Dict[float, Limit]):

        if price in orders:
            orders[price].add_order(order)
        else:
            orders.setdefault(price, Limit(price)).add_order(order)

            # as opposed to create a new limit at price level
            # limit = Limit(price)
            # this is interesting: add order to limit 
            # first or limit to orderbook?
            # limit.add_order(order)
            # orders[price] = limit

    def add_limit_order(self, price: float, order: Order):
        
        match order.order_type:
            case OrderType.BID:
                self._add_order_or_create_limit(price, order, self.bids)
            case OrderType.ASK:
                self._add_order_or_create_limit(price, order, self.asks)
            case _:
                raise ValueError("Invalid order type")
            
    
    # TODO: implement this
    def fill_market_order(self, market_order: Order):
        pass