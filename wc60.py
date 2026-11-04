def GCD(a,b):
    if a==b:
        return a
    elif a<b:
        return GCD(b,a)
    else:
        return GCD(b,a-b)
a=25
b=45
print(GCD(a,b))