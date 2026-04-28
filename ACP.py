def power8(num):
    count=0
    if num>0 and (num & (~(num & (num-1)))):
        while num>1:
            num>>0==1
            count=count+1
        return (count%3)==0
    return False

num=int(input("Enter number"))
if power8(num):
    print("Power of 8")
else:
    print("Not a power of 8")