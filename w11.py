def make_payment(balance,amount):
    try:
        amount=float(amount)
        if amount<=0:
            raise ValueError("amount must be positive")
        if amount>balance:
            raise ValueError("insufficient balance")
        balance=amount
        print(f"paid{amount}.new balance:{balance}")
    except ValueError as e:
        print("payment failed:",e)
    finally:
        print("transaction attempt finished")

make_payment(1000,300)
make_payment(1000,"abc")
make_payment(1000,5000)
 