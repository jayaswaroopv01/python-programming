n=int(input("enter the numbers of terms:\t"))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
    print("the sum of series is",round(sum1,2))