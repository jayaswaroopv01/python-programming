a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))
d=int(input("enter num4:"))
if(a>b and a>c and a>d):
    print("greatest number is:",a)
elif(b>c and b>d):
    print("greatest number is:",b)
elif(c>d):
    print("greatest number is:",c)
elif(d>c):
    print("greatest number is:",d)
else:
    print("wrong values")
