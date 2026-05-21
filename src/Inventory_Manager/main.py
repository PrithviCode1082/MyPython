from utils import print_inventory, print_inventory_keys

def menu():
    print("1 - Add Supplies\n2 - Move Supplies to Shop\n3 - Check Supplies\n4 - And new Aisle\n5 - Exit")

managing = True

while managing:
    menu()
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            print_inventory_keys()
        case _:
            break
