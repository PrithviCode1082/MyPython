import math as Math

def valueChecker(num):
    return "Negative" if (num < 0) else "Zero" if (num == 0) else "Positive" 

def even_odd(num):
    return "Even" if (num % 2 == 0) else "Odd"

def perfect_square(num):
    square = int(Math.sqrt(num))
    return f"{num} is a Perfect Square of {square}" if (square * square == num) else "is not a perfect square"

number = int(input("Enter a number: "))
print(f"Number {number} is {valueChecker(number)}")
print(f"Number {number} is {even_odd(number)}")
print(f"Number {perfect_square(number)}")
