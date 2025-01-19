from typing import List

from .order import Order


class Limit:
    def __init__(self, price: float):
        self.price: float = price
        self.orders: List[Order] = []

    def __str__(self):
        return f"{self.total_volume}@${self.price}[{len(self.orders)}]"

    def __repr__(self):
        return str(self)

    def add_order(self, order: Order):
        self.orders.append(order)

    @property
    def total_volume(self):
        return sum([order.quantity for order in self.orders])

    def fill_order(self, market_order: Order):
        for limit_order in self.orders:
            match market_order.quantity >= limit_order.quantity:
                case True:
                    market_order.quantity -= limit_order.quantity
                    limit_order.quantity = 0.0
                case False:
                    limit_order.quantity -= market_order.quantity
                    market_order.quantity = 0.0

            if market_order.is_filled:
                break

        # TODO: remove filled orders
