n=int(input("enter a number"))
factorial=1
if n<0:
    print("sorry,factorial doesnot exist for negative number")
elif n==0:
    print("the factorial of 0 is 1:")
else:
    for i in range(1,n+1):
        factorial=factorial*i
print("the factorial of",n,"is",factorial)