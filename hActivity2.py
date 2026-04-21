def power4(num):
    count=0
    if (num & (~(num & (num-1)))): #Check if power of 2
        while (num>1):
            num>>=1
            count=count+1
        if (count%2)==0:
            return True
        else:
            return False
        
num=int(input("Enter a number"))

if (power4(num)):
    print(f"{num} is a power of 4")
else:
    print(f"{num} is not a power of 4")