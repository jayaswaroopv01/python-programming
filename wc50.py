person=dict()
n=int(input("enter the number of persons:"))
for i in range(n):
    sname=str(input("enter name of persons:"))
    for j in range(1):
        password=int(input("enter the password:"))
        person[sname]=password
print("created dictionary of person along with password:",person)
person.clear()
print(person)
