import unittest
from item import Item

class TestItem(unittest.TestCase):
    def test_item(self):
        item = Item('123', 1, 'test', 1.00)
        self.assertEqual(item.create_item(), {'123': {'quantity': 1, 'name': 'test', 'price': 1.00}})
        self.assertEqual(item.get_sku(), '123')
        self.assertEqual(item.get_quantity(), 1)
        self.assertEqual(item.get_name(), 'test')
        self.assertEqual(item.get_price(), 1.00)