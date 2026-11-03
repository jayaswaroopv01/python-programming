import array as arr
a=arr.array('i',[10,43,21,-1,89,45,49,98,32])
print(a)
flag=0
key=int(input("enter the key element to be search"))
for i in a:
    if i==key:
        flag=1
        break
if flag==1:
    print("search is successful")
else:
    print("search is unsuccessful")