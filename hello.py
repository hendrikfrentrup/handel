import sys

import engine

from engine.orderbook import (Limit, Order, OrderBook, OrderType)

def main():
    print(sys.path)
    
    print(dir(engine))
    print(engine.__path__)
    
    bid = OrderType.BID
    ask = OrderType.ASK
    
    print(bid)
    order = Order(bid, 100)
    print(order)
    # print(order.is_filled)
    # order.quantity-=100
    # print(order.is_filled)

    limit = Limit(113.2)
    print(limit)
    limit.add_order(order)
    print(limit)
    for qty in range(100, 60, -10):
        limit.add_order(Order(bid, qty))
    print(limit)

    order_book = OrderBook()
    print(order_book)
    order_book.add_limit_order(113.2, order)
    print(order_book)

    print("Zeit zum handeln!")

# test create buy order
# test create another buy order
# add order to orderbook
# create sell order
# create market order

if __name__ == "__main__":
    # 
    
    main()
