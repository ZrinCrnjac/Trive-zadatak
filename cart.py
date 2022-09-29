from item import Item
class Cart():
    def __init__(self):
        self.items = {}
    def add_item(self, sku, quantity):
        self.items[sku] = int(quantity)
    def get_item_cart(self, sku):
        return self.items[sku]
    def get_items(self):
        return self.items
    def remove_item(self, sku):
        del self.items[sku]
    def update_item(self, sku, quantity):
        self.items[sku] -= quantity
        if(self.items[sku] == 0):
            self.remove_item(sku)
    def print_items(self):
        for item in self.items:
            print(item)
    def get_total(self, storage):
        total = 0
        for attr, value in self.items.items():
            total += int(storage.get_item(attr).get_price()) * int(value)
        return total
    def checkout(self):
        self.items = {}
    def print_receipt(self, storage):
        for attr, value in self.items.items():
            item = storage.get_item(attr)
            print(item.get_name(), value, 'x' ,item.get_price(), '=', (int(value)*int(item.get_price())))
        print("TOTAL: " + str(self.get_total(storage)))