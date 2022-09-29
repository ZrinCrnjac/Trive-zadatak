import unittest
from item import Item
from storage import Storage
from cart import Cart

class TestCart(unittest.TestCase):
    def test_cart(self):
        cart = Cart()
        cart.add_item('123', '1')
        self.assertEqual(cart.get_item_cart('123'), 1)
        self.assertEqual(cart.get_items(), {'123': 1})
        cart.remove_item('123')
        self.assertEqual(cart.get_items(), {})
        cart.add_item('123', 5)
        cart.update_item('123', 3)
        self.assertEqual(cart.get_item_cart('123'), 2)
        cart.checkout()
        self.assertEqual(cart.get_items(), {})
        cart.add_item('123', 5)
        cart.update_item('123', 3)
        cart.checkout()
        self.assertEqual(cart.get_items(), {})
        storage = Storage()
        storage.add_item(Item('123', '1', 'test', '1'))
        storage.add_item(Item('456', '1', 'test', '2'))
        cart.add_item('123', 5)
        cart.add_item('456', 3)
        self.assertEqual(cart.get_total(storage), 11)
        cart.checkout()
        self.assertEqual(cart.get_items(), {})
        cart.add_item('123', 5)
        cart.add_item('456', 3)
        cart.print_receipt(storage)
        cart.checkout()
        self.assertEqual(cart.get_items(), {})
        cart.add_item('123', 5)
        cart.add_item('456', 3)
        cart.print_items()
        cart.checkout()
        self.assertEqual(cart.get_items(), {})

