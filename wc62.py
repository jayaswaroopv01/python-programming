import datetime
import random
print(datetime.datetime.now())
x=datetime.datetime.now()
print("year:",x.year)
print(random.random())
print("the random number between 1 and 10 is:",random.randint(1,10))
print("the random number between 5 and 25 is:",random.randint(5,25))
print("the random number between -10 and -2 is:",random.randint(-10,-2))
s1="BENGALURU"
print("the random value from string is:",random.choice(s1))
t1=(44,55,33,22,11)
print("the random value from list is:",random.choice(t1))
l1=["apple","banana","cherry"]
print("the random value from list is:",random.choice(l1))
random.shuffle(l1)
print("the list afterbshuffle:",l1)
random.shuffle(l1)
print("the list after second shuffle:",11)