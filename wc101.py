import heapq
tup=(5,20,3,7,6,8)
k=2
j=heapq.nsmallest(k,tup)
y=heapq.nlargest(k,tup)
print(j)
print(y)
