# h = (q + (13(m+1) / 5) + K + (k / 4) + (J / 4) - 2J) % 7
# h = day of the week (0 - 6)
# q = day of the month
# m = month (1-12)
# k = year of the century (year % 100)
# j = Zero based century (year / 100)

nums = [0, 1, 2, 3, 4, 5, 6]

def getDay(q, m, K, J, y):
    if m < 3:
        m += 12
        y -= 1
    K = y % 100
    J = y // 100
    return (q + (13 * (m + 1) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7

    

def printDigit(digit):
    if(len(str(digit)) > 1):
        print(f"{digit} ", end=" ")
    else:
        print(f"0{digit} ", end=" ")

q = int(input("Enter day of the month (1-31): "))
m = int(input("Enter month of the year: "))
y = int(input("Enter the year: "))
K = 0
J = 0

actual = getDay(q, m, K, J, y)
first = getDay(1, m, K, J, y)
nextFirst = getDay(1, m+1, K, J, y)

dayCount = 1
feb = False
checker = [30, 31]
if m < 3:
    feb = True
    checker = [28, 29]

def check(current, nextFirst):
    if(getDay(current, m, K, J, y) == 6 and nextFirst == 0):
        return True
    return getDay(current, m, K, J, y) == (nextFirst - 1)


print("Sat Sun Mon Tue Wed Thu Fri")
for i in range(0, 6):
    for j in nums:
        if(j >= first or (i != 0)):
            printDigit(dayCount)
            if (dayCount in checker):
                if check(dayCount, nextFirst):
                    print()
                    exit()
            dayCount += 1
        else:
            print(" * ", end=" ")
    print()