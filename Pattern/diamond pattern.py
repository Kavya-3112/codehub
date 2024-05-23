row=int(input())
m=row
for i in range(1,row+1):
    print(" "*(row-i)+"* "*i)
for j in range(row):
    print(" "*(j+1)+"* "*(row-j-1))
