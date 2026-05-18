items = {
    "Groceries": {
        "Egg": 2,
        "Milk": 20,
        "Flour": 40,
        "Apple": 3,
    },
    "Chips": {
        "Classic Salted": 5,
        "Spicy Jalapeño": 6,
        "Sour Cream & Onion": 7,
        "BBQ Blast": 6,
    },
    "Soda": {"Cola": 10, "Lemon Lime": 9, "Orange": 9},
    "Bread": {"Whole Wheat": 15, "White": 12, "Multigrain": 18},
    "Coffee Beans": {"Dark Roast": 50, "Light Roast": 45, "Decaf": 48},
}


def menu():
    print(" ------ Menu ------")
    i = 1
    for k in items.keys():
        print(f"{i}) {k} ")
        i += 1
    print("--------------------")


def itemIterate(section):
    i = 1
    for k, v in items[section].items():
        print(f"{i}) {k} - ${v}")
        i += 1


def add_item(cart):
    running = True
    secId, itemId, quantity = 0, 0, 0
    menu()
    secId = int(input("Enter the section ID: ")) - 1
    section = list(items.keys())[secId]
    itemIterate(section)
    while running:
        itemId = int(input("Enter the item ID: ")) - 1
        item = list(items[section].keys())[itemId]
        quantity = int(input(f"Enter quantity for {item}: "))
        print(f"{item} has been added successfully!")
        if item in cart.keys():
            cart[item] += quantity
        else:
            cart[item] = quantity
        choice = input("Add Another Item? Type 'Y' for yes and 'N' for no: ")
        if choice == "n":
            return


def printCart(cart):
    if len(cart) == 0:
        print("Cart is empty!")
        return 0
    print("----- CART -----")
    i = 1
    for k, v in cart.items():
        print(f"{i}) {k} - {v}")
        i += 1
    return 1
