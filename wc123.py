s1="geeks for geeks"
s2="learning from geeks for geeks"
words=(s1+""+s2).split()
res=[]
for word in words:
    if words.count(word)==1:
        res.append(word)
print(res)
