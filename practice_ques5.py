# Practice Question 5:
# Create a class called order which stores item and its price
# Use dunder function __gt__() to convey that
# order1 > order2. if price of order1 is greater than price of order2

class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2): # (greater than) dunder function
        return self.price > order2.price

order1 = Order("chips", 50)
order2 = Order("eggs", 20)
print(order1 > order2)