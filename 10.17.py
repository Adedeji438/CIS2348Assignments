class ItemToPurchase:
    def __init__(self, n= "none", p = 0, q = 0):
        self.item_name = n
        self.item_price = p
        self.item_quantity = q

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str( self.item_price * self.item_quantity ))

if __name__ == "__main__":
    print("Item 1")
    
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item1 = ItemToPurchase(name, price, quantity)
    print()
    print("Item 2")
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item2 = ItemToPurchase(name, price, quantity)
    print()
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = (item1.item_price*item1.item_quantity)+(item2.item_price * item2.item_quantity)
    print()
    print("Total: $" + str(total))
