import unittest
from item import Item
from storage import Storage

class TestStorage(unittest.TestCase):
    def test_storage(self):
        storage = Storage()
        storage.add_item(Item('123', '1', 'test', '1'))
        self.assertEqual(storage.get_item('123').get_sku(), '123')
        self.assertEqual(storage.get_item('123').get_quantity(), '1')
        self.assertEqual(storage.get_item('123').get_name(), 'test')
        self.assertEqual(storage.get_item('123').get_price(), '1')
        storage.remove_item('123')
        self.assertEqual(storage.get_items(), {})