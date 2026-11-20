j="hello world"
freq={}
for char in j:
    freq[char]=freq.get(char,0)+1
max_char=max(freq,key=freq.get)
print(max_char)
