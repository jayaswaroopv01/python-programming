balance=5000
print("1.deposite")
print("2.withdraw")
choice=input("choice:")
amount=int(input("amount:"))
if choice=='1':
    balance+=amount
elif choice=='2' and amount<=balance:
    balance-=amount
print("balance is:",balance)

    