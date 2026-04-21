def power(num):
    if (num==0):
        return 0
    if ((num & (~(num-1)))==num):
        return 1
    return 0

num=int(input("Enter a number"))

if (power(num)):
    print("The number is power of 2")
else:
    print("The number is not a power of 2")