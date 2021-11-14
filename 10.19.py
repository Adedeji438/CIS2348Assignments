class ItemToPurchase:
    def __init__(self, n = 'none', p = 0, q = 0, d = 'none'):
        self.item_name = n
        self.item_description = d
        self.item_price = p
        self.item_quantity = q

    def print_item_cost(self):
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, n = "none", d= "January 1, 2016", c = []):
        self.customer_name = n
        self.current_date = d
        self.cart_items = c

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, name):
        if name == "":
            return
        isFound = False
        for i in self.cart_items:
            if i.item_name == name:
                self.cart_items.remove(i)
                isFound = True
                break
        if not isFound:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        isFound = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                self.cart_items[i].item_quantity = item.item_quantity
                isFound = True
                break
        if not isFound:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        numItems = 0
        for i in self.cart_items:
            numItems += i.item_quantity
        return numItems

    def get_cost_of_cart(self):
        cost = 0
        for i in self.cart_items:
            cost += (i.item_quantity * i.item_price)
        return cost

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items: %d\n' % self.get_num_items_in_cart())
        cost = self.get_cost_of_cart()
        if (cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            for i in self.cart_items:
                i.print_item_cost()
        print('\nTotal: $%d' % cost)

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for i in self.cart_items:
                i.print_item_description()


def print_menu(cart):
    currentCart = cart
    cmd = ''
    while (cmd != 'q'):
        print('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            "i - Output items' descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n')
        cmd = input('Choose an option:\n')
        while (
                cmd != 'a' and cmd != 'o' and cmd != 'i' and cmd != 'q' and cmd != 'r' and cmd != 'c'):
            cmd = input('Choose an option:\n')
        if (cmd == 'a'):
            print("\nADD ITEM TO CART")
            name = input('Enter the item name:\n')
            description = input('Enter the item description:\n')
            price = int(input('Enter the item price:\n'))
            quantity = int(input('Enter the item quantity:\n'))
            newItem = ItemToPurchase(name, price, quantity, description)
            currentCart.add_item(newItem)
        elif (cmd == 'r'):
            print('REMOVE ITEM FROM CART')
            removeItem = input('Enter name of item to remove:\n')
            currentCart.remove_item(removeItem)
        elif (cmd == 'c'):
            print('\nCHANGE ITEM QUANTITY')
            name = input('Enter the item name:\n')
            qty = int(input('Enter the new quantity:\n'))
            changeItem = ItemToPurchase(name, 0, qty)
            currentCart.modify_item(changeItem)
        elif (cmd == 'i'):
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            currentCart.print_descriptions()
        elif (cmd == 'o'):
            print('OUTPUT SHOPPING CART')
            currentCart.print_total()

if __name__ == "__main__":
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print("\nCustomer name: %s" % name)
    print("Today's date: %s" % date)
    cart = ShoppingCart(name, date)
    print_menu(cart)