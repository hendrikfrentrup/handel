from engine.order import Order, OrderType
from engine.limit import Limit

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
    
def test_limit_fill_order_partial():
    limit = Limit(10.0)
    limit_order = Order(OrderType.BID, 100.0)
    limit.add_order(limit_order)
    
    market_order = Order(OrderType.ASK, 60.0)
    limit.fill_order(market_order)
    
    assert market_order.is_filled
    assert limit_order.quantity == 40.0
    assert limit.total_volume == 40.0

def test_limit_fill_order_complete():
    limit = Limit(10.0)
    limit_order = Order(OrderType.BID, 50.0)
    limit.add_order(limit_order)
    
    market_order = Order(OrderType.ASK, 100.0)
    limit.fill_order(market_order)
    
    assert not market_order.is_filled
    assert market_order.quantity == 50.0
    assert limit_order.quantity == 0.0
    assert limit.total_volume == 0.0

def test_limit_fill_multiple_orders():
    limit = Limit(10.0)
    limit.add_order(Order(OrderType.BID, 50.0))
    limit.add_order(Order(OrderType.BID, 50.0))
    
    market_order = Order(OrderType.ASK, 75.0)
    limit.fill_order(market_order)
    
    assert market_order.is_filled
    assert limit.orders[0].quantity == 0.0
    assert limit.orders[1].quantity == 25.0
    assert limit.total_volume == 25.0