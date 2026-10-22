employees=[
    {"name":"asha","salary":55000},
    {"name":"kiran","salary":48000},
]
total=0
heighest=None
for e in employees:
    total += e["salary"]
    if heighest is None or e["salary"] > heighest["salary"]:
        heighest = e
print("Total salary:",total)
if heighest:
    print(f"heighest paid:{heighest['name']},salary: {heighest['salary']}")