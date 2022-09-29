class Item:
    def __init__(self, sku, quantity, name, price):
        self.sku = sku
        self.quantity = quantity
        self.name = name
        self.price = price
    def create_item(self):
        return {self.sku: {'quantity': self.quantity, 'name': self.name, 'price': self.price}}
    def get_sku(self):
        return self.sku
    def get_quantity(self):
        return self.quantity
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
