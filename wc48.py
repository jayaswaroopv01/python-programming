a=[[1,2,3,],[4,5,6,],[9,8,7,]]
b=[[4,3,2,],[5,4,3,],[4,3,2,]]
c=[[0,0,0],[0,0,0],[0,0,0]]
r=len(a)
col=len(a[0])
for i in range(0,r):
    for j in range(0,col):
        c[i][j]=a[i][j]+b[i][j]
        print("matrix addition is...")
        for k in c:
            print(k)