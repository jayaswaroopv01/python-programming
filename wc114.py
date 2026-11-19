s="python is great"
wrds=s.split()
even_words=filter(lambda w:len(w)%2==0,wrds)
res="".join(even_words)
print(res)
