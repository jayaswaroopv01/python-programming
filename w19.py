pin=1234
count=0

while True:
    if count==3:
        break
    pin_input=int(input("enter 4-digit pin:"))
    if pin==pin_input:
        print("access granted:")
    else:
        print("wrong pin. try again")
    count += 1
if count == 3:
    print("account locked. too many attempts!!")