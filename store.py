from item import Item
from storage import Storage
from cart import Cart
parsed_string = ['START']
storage = Storage()
while len(parsed_string)!=0 and parsed_string[0]!='END':
    item = input()
    parsed_string = item.split(" ")
    if(len(parsed_string) == 5):
        command = parsed_string[0]
        sku = parsed_string[1]
        quantity = parsed_string[2]
        name = parsed_string[3]
        price = parsed_string[4]
        if(parsed_string[0] == 'ADD'):
            item = Item(parsed_string[1], parsed_string[2], parsed_string[3], parsed_string[4])
            storage.add_item(item)
        else:
            print("Invalid command")

parsed_string = ['START']
cart = Cart()

while len(parsed_string)!=0 and parsed_string[0]!='END':
    item = input()
    parsed_string = item.split(" ")
    if(len(parsed_string) == 3):
        command = parsed_string[0]
        sku = parsed_string[1]
        quantity = parsed_string[2]
        if(parsed_string[0] == 'ADD'):
            cart.add_item(sku, quantity)
            if(int(quantity)>int(storage.get_item(sku).get_quantity())):
                print("Not enough items in stock!")
                cart.remove_item(sku)
            elif(int(quantity)<0):
                print("Invalid quantity!")
                cart.remove_item(sku)
        elif(parsed_string[0] == 'REMOVE'):
            if(sku not in cart.get_items()):
                print("Item not in cart!")
            elif(int(quantity)>int(cart.get_item_cart(sku))):
                print("Not enough items in cart!")
            elif(int(quantity)<0):
                print("Invalid quantity!")
            elif(int(quantity)==0):
                print("Cannot remove 0 items!")
            else:
                cart.update_item(sku, int(quantity))
        else:
            print("Invalid command")
    elif(parsed_string[0] == 'CHECKOUT'):
        cart.print_receipt(storage)
        cart.checkout()
