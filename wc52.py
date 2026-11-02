x=eval(input("enter the list:"))
key=int(input("enter the number to be searched:"))
found=0
for i in x:
    if i==key:
        found=1
        break
if found==1:
    print("success")
else:
    print("unsuccess")