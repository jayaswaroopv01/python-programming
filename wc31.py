marks=float(input("enter the marks:"))
if marks<0.0 or marks>1.0:
    print("marks is invalid")
elif marks>=0.9:
    print("grade=a")
elif marks>=0.8:
    print("grade=b")
elif marks>=0.7:
    print("grade=c")
elif marks>=0.6:
    print("grade=d")
else:
    print("grade=f")