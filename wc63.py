x=input("enter value of x:")
y=input("enter value of y:")
try:
    result=int(x)/int(y)
except ZeroDivisionError:
    print("division by zero!")
else:
    print(f"result is(result)")
finally:
    print("executing finally clause")
