from engine.order import Order, OrderType

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