m=[ [1,2,3],
    [5,6,8],
    [7,8,9]
    ]
res=[
    [0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(m)):
    for j in range(len(m[0])):
        res[j][i]=m[i][j]
for k in res:
    print(k)
