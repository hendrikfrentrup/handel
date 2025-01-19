import pytest
from engine.orderbook import OrderBook
from engine.order import Order, OrderType

@pytest.fixture
def orderbook():
    return OrderBook()

@pytest.fixture
def bid_order():
    return Order(OrderType.BID, 100)

@pytest.fixture 
def ask_order():
    return Order(OrderType.ASK, 100)

def test_orderbook_init(orderbook):
    assert len(orderbook.asks) == 0
    assert len(orderbook.bids) == 0

def test_add_limit_bid_order(orderbook, bid_order):
    orderbook.add_limit_order(10.0, bid_order)
    assert len(orderbook.bids) == 1
    assert 10.0 in orderbook.bids
    assert orderbook.bids[10.0].orders[0] == bid_order

def test_add_limit_ask_order(orderbook, ask_order):
    orderbook.add_limit_order(10.0, ask_order)
    assert len(orderbook.asks) == 1
    assert 10.0 in orderbook.asks
    assert orderbook.asks[10.0].orders[0] == ask_order

def test_add_multiple_orders_same_limit(orderbook):
    bid1 = Order(OrderType.BID, 100)
    bid2 = Order(OrderType.BID, 100)
    orderbook.add_limit_order(10.0, bid1)
    orderbook.add_limit_order(10.0, bid2)
    assert len(orderbook.bids) == 1
    assert len(orderbook.bids[10.0].orders) == 2

def test_invalid_order_type(orderbook):
    invalid_order = Order("INVALID", 100)
    with pytest.raises(ValueError, match="Invalid order type"):
        orderbook.add_limit_order(10.0, invalid_order)

def test_fill_market_buy_order(orderbook):
    # Add ask limit orders
    ask1 = Order(OrderType.ASK, 50)
    ask2 = Order(OrderType.ASK, 50)
    orderbook.add_limit_order(10.0, ask1)
    orderbook.add_limit_order(11.0, ask2)

    # Create market buy order
    market_buy = Order(OrderType.BID, 75)
    orderbook.fill_market_order(market_buy)

    assert ask1.is_filled
    assert ask2.quantity == 25
    assert market_buy.quantity == 0

def test_fill_market_sell_order(orderbook):
    # Add bid limit orders
    bid1 = Order(OrderType.BID, 50)
    bid2 = Order(OrderType.BID, 50)
    orderbook.add_limit_order(10.0, bid1)
    orderbook.add_limit_order(9.0, bid2)

    # Create market sell order
    market_sell = Order(OrderType.ASK, 75)
    orderbook.fill_market_order(market_sell)

    assert bid1.is_filled
    assert bid2.quantity == 25
    assert market_sell.quantity == 0

def test_orderbook_str_representation(orderbook):
    orderbook.add_limit_order(10.0, Order(OrderType.BID, 100))
    orderbook.add_limit_order(11.0, Order(OrderType.ASK, 100))
    assert str(orderbook) == "asks: 1, bids: 1"

def test_orderbook_str_representation(orderbook):
    assert isinstance(repr(orderbook), str)

def test_ask_limits_sorting(orderbook):
    orderbook.add_limit_order(12.0, Order(OrderType.ASK, 100))
    orderbook.add_limit_order(10.0, Order(OrderType.ASK, 100))
    orderbook.add_limit_order(11.0, Order(OrderType.ASK, 100))
    
    limits = orderbook._ask_limits
    assert [limit.price for limit in limits] == [10.0, 11.0, 12.0]

def test_bid_limits_sorting(orderbook):
    orderbook.add_limit_order(12.0, Order(OrderType.BID, 100))
    orderbook.add_limit_order(10.0, Order(OrderType.BID, 100))
    orderbook.add_limit_order(11.0, Order(OrderType.BID, 100))
    
    limits = orderbook._bid_limits
    assert [limit.price for limit in limits] == [12.0, 11.0, 10.0]