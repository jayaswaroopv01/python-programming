j="python is fun"
words=j.split()
res=""
for word in reversed(words):
    res+=word+""
res=res.strip()
print(res)