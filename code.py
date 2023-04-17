class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total_cost = 0.0

    def invariant(self):
        assert self.total_cost >= 0, "Total cost must be non-negative."

    def add_item(self, item, quantity):
        assert quantity > 0, "Quantity must be greater than 0."
        self.items[item] = self.items.get(item, 0) + quantity
        self.total_cost += item.price * quantity
        self.invariant()

    def checkout(self, payment_method):
        assert len(self.items) > 0, "Cannot checkout an empty cart."
        # Process the payment and clear the cart
        print("Processing payment of", self.total_cost, "using", payment_method)
        self.items = {}
        self.total_cost = 0
        self.invariant()

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Sample usage:
cart = ShoppingCart()
item1 = Item('Apple', 1.0)
item2 = Item('Banana', 0.5)

cart.add_item(item1, 3)
cart.add_item(item2, 2)
cart.checkout('Credit Card')
