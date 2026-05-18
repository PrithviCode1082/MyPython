from ShoppingCart import *

cart = {}
temp = 0
total_bill = 0


def choices():
    print("1 - Add Item\n2 - Remove/Edit Item\n3 - See Cart\n4 - Finish")


shopping = True
while shopping:
    choices()
    choice = int(input("Enter a choice: "))
    match choice:
        case 1:
            add_item(cart)
            print()
        case 2:
            if printCart(cart) != 0:
                temp = (
                    int(input("Enter the ID of item you want to Edit or remove: ")) - 1
                )
                item = list(cart.keys())[temp]
                temp = int(input("Edit (Type 1) or Remove (Type 2)"))
                if temp == 1:
                    quan = int(input(f"Enter new quantity for {item}: "))
                    cart[item] = quan
                else:
                    del cart[item]
                    print(f"{item} was removed successfully")
            print()
        case 3:
            printCart(cart)
            print()
        case _:
            for section in items.keys():
                for k, v in cart.items():
                    if k in items[section].keys():
                        print(f"{k}  -   {v}   -  ${items[section][k] * v}")
                        total_bill += items[section][k] * v
            print(f"Your total bill is: ${total_bill}")

            break
