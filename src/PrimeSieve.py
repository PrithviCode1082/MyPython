length = 50

nums = [num for num in range(3, length)]


value = 2
while(value < length):
    for i in nums:
        if(i % value == 0 and i != value):
            nums.remove(i)
    value = value+1
    if((value * value) >= length):
        break

[print(num) for num in nums]
