s=set()
for i in range(50,100):
    if(i%6==0):
        s.add(i)
print(s)
print("the deleted no is:",s.pop())
print("after deletion the set is")
print(s)
s.add(105)
print("after adding 101 the set")
print(s)