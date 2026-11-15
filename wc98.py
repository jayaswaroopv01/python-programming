j=int(input("principal amount:"))
y=(int(input("rate of interest:")))
a=int(input("time in years:"))
amt=j*(pow((1+y/100),a))
ci=amt-j
print("compound interest:",ci)
