x=[[1,2],[3,4],[5,6]]
y=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        y[j][i]=x[i][j]
        print("transpose of a given matrix is...")
        for r in y:
            print(r)
