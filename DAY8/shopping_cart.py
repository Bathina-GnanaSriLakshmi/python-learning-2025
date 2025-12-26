#To build  a shopping cart 
cart = []
def add_cart(cart,item):
    cart += [item]
    print(f"{item} is successfully added in the cart")
    return cart
def remove_cart(cart,item):
    new_cart = []
    if item in cart:
        for i in cart :
            if i != item:
                new_cart += [i]
            else :
                print(f"{item} is removed from the cart")
        cart = new_cart
        return cart
    else:
        print("{item} doesn't exist in the cart")
        return cart
o = 1
while o != 5:
    print("MENU: ")
    print("1.add to cart \n 2.remove an item from the cart \n 3.items in the cart \n 4.Clear the cart \n 5.EXit")
    o = int(input("Enter your option: "))
    if o == 1:
        item = input("Enter item: ")
        cart = add_cart(cart,item)
    elif o == 2:
        item = input("Enter the item you want to remove: ")
        cart = remove_cart(cart,item)
    elif o == 3:
        print(cart)
    elif o == 4:
        cart = []
    elif o == 5:
        print("Exiting...")
    else:
        print("Enter valid options")