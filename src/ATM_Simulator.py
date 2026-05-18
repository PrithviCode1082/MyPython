pin = 5161
chances = 3
balance = 2000
transaction_history = []
choice = 1

def checkPin(): return int(input("Enter your pin: "))
def getAmount(): return int(input("Enter the amount: "))

def menu():
    print("***** MENU *****")
    print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")

while choice in [1, 2, 3, 4, 5]:
    menu()
    choice = int(input("Enter a choice: "))
    get_pin = checkPin()
    while(pin != get_pin):
        chances -= 1;
        print("Your pin is wrong")
        if(chances == 0):
            print("You've entered pin wrong for 3 times!!!")
            exit()
        get_pin = checkPin()

    match(choice):
        case 1:
            amount = getAmount()
            balance += amount
            print("Deposited successfully!")
            transaction_history.append(f"${amount} deposited successfully")
        case 2:
            amount = getAmount()
            if(amount > balance):
                print("You don't have enough balance")
                continue
            balance -= amount
            transaction_history.append(f"${amount} withdrawn successfully")
        case 3:
            print("Your balance is: ", balance)
        case 4:
            print("***** Transaction History ******")
            [print(f"* {transaction}") for transaction in transaction_history]
        case _:
            exit()

        