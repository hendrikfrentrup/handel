from enum import Enum

class OrderType(Enum):
    BID = "Bid"
    ASK = "Ask"

class Order:
    def __init__(self, order_type: OrderType, quantity: float):
        self.order_type: OrderType = order_type
        self.quantity: float = quantity
    
    @property
    def is_filled(self):
        return self.quantity == 0.0
    
    def __str__(self):
        return f"{self.order_type.value} for {self.quantity}"

    def __repr__(self):
        return str(self)