def count_up_to(max):
    count=1
    while count<=max:
        yield count
        count+=1
print(list(count_up_to(3)))