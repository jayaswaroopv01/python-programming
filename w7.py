def total_size(folder):
    total=0
    for item in folder:
        if isinstance(item,list):
            total+=total_size(item)
        else:
            total+=item
    return total
disk=[10,20,[5,5,[2,3],50]]
print("total size:",total_size(disk),"kb")