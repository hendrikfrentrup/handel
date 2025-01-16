def test_engine_import():
    import engine

from engine.orderbook import Limit
from engine.orderbook import Order, OrderType


def test_order_creation():
    
    bid = Order(OrderType.BID, 100.0)
    ask = Order(OrderType.ASK, 50.0)
    
    assert bid.order_type == OrderType.BID
    assert bid.quantity == 100.0
    assert not bid.is_filled
    
    assert ask.order_type == OrderType.ASK
    assert ask.quantity == 50.0
    assert not ask.is_filled

def test_order_str():
    
    order = Order(OrderType.BID, 100.0)
    assert str(order) == "Bid for 100.0"
    
def test_limit_creation():
    limit = Limit(10.0)
    assert limit.price == 10.0
    assert len(limit.orders) == 0
    assert limit.total_volume == 0.0

def test_limit_add_order():
    limit = Limit(10.0)
    order = Order(OrderType.BID, 100.0)
    limit.add_order(order)
    
    assert len(limit.orders) == 1
    assert limit.total_volume == 100.0

def test_limit_multiple_orders():
    limit = Limit(10.0)
    limit.add_order(Order(OrderType.BID, 100.0))
    limit.add_order(Order(OrderType.BID, 50.0))
    
    assert len(limit.orders) == 2
    assert limit.total_volume == 150.0

def test_limit_str():
    limit = Limit(10.0)
    limit.add_order(Order(OrderType.BID, 100.0))
    
    assert str(limit) == "100.0@$10.0[1]"

def test_limit_empty_str():
    limit = Limit(10.0)
    assert str(limit) == "0@$10.0[0]"
