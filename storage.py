class Storage:
    def __init__(self):
        self.items = {}
    def add_item(self, item):
        self.items[item.get_sku()] = item
    def get_item(self, sku):
        return self.items[sku]
    def get_items(self):
        return self.items
    def remove_item(self, sku):
        del self.items[sku]
    def print_items(self):
        for item in self.items:
            print(self.items[item])
    