def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
        return-1
arr=[10,23,45,70,11,15]
x=70
res=linear_search(arr,x)
if res!=-1:
    print("element found at index:",res)
else:
    print("element not found in the array")
    