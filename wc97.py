from collections import defaultdict
s="geeksforgeeks"
d=defaultdict(int)
for c in s:
    d[c]+=1
res=[c for c in d if d[c]>1]
print(res)
