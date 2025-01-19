
from typing import Dict, List

from .order import Order, OrderType
from .limit import Limit

class OrderBook:
    def __init__(self):
        self.asks: Dict[float, Limit] = {}
        self.bids: Dict[float, Limit] = {}
    
    def __str__(self):
        return f"asks: {len(self.asks)}, bids: {len(self.bids)}"

    def __repr__(self):
        return str(self)
    
    @property
    def _ask_limits(self) -> List[Limit]:
        return sorted(self.asks.values(), key=lambda limit: limit.price)
    
    @property
    def _bid_limits(self) -> List[Limit]:
        return sorted(self.bids.values(), key=lambda limit: -limit.price)
    
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

    # TODO: determine if limit or market order and fill or add to orderbook based on price

    def add_limit_order(self, price: float, order: Order) -> None:
        
        match order.order_type:
            case OrderType.BID:
                self._add_order_or_create_limit(price, order, self.bids)
            case OrderType.ASK:
                self._add_order_or_create_limit(price, order, self.asks)
            case _:
                raise ValueError("Invalid order type")
            
    def fill_market_order(self, market_order: Order) -> None:
        match market_order.order_type:
            case OrderType.BID:
                limits = self._ask_limits
            case OrderType.ASK:
                limits = self._bid_limits
            case _:
                raise ValueError("Invalid order type")
            
        for limit in limits:
            limit.fill_order(market_order)
            if market_order.is_filled:
                break