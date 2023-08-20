n=int(input())
for i in range(0,n):
    x=input()
    length=len(x)
    if length >10:
        print(x[0],end='')
        print(length-2,end='')
        print(x[length-1])
    else:
        print(x)
