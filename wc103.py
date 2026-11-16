t=[(15,3),(3,9),(1,10),(99,22)]
j=''
for x in t:
    for y in x:
        j+=str(y)
res=list(map(int,set(j)))
print(res)