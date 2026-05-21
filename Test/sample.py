original = 133
test = original
length = len(f"{original}")
rem = ""

def getSum(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum


for i in range(0, length):
    rem = f"{rem}{original%10}"
    original = int(original / 10)

if (int(rem) == test):
    print("Palindrome!")
    print(f"Sum is {getSum(rem)}")
else:
    print(f"Sum is {getSum(rem)}")
